from constance import config
from django import forms
from django.conf import settings
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string
from django.utils import simplejson
from robinson.models import *
from sorl.thumbnail import get_thumbnail
import urllib


def json_markers(request):
    """
    Returns the latitude/longitude coordinates for all of the valid photos
    as well as basic information about them. The data returned is serialized
    as JSON.
    """
    if not request.is_ajax():
        raise Http404
    markers = dict()
    for photo in Photo.objects.all():
        # Skip the current photo if it is not valid, i.e. was automatically
        # imported and no geolocation information has been set yet
        if not photo.is_valid():
            continue
        # Use the latest EXIF tag as the date at which the picture was taken
        date_taken = photo.exiftag_set.filter(key='Exif.Image.DateTime').latest('value').value
        marker_details = dict()
        marker_details['acc'] = photo.get_location_accuracy_display()
        marker_details['dt'] = date_taken
        marker_details['ele'] = photo.get_elevation()
        marker_details['lat'] = photo.latitude
        marker_details['loc'] = photo.get_location()
        marker_details['lon'] = photo.longitude
        marker_details['thumb_url'] = get_thumbnail(photo.file, settings.PHOTO_THUMBNAIL_SIZE, crop='noop').url
        markers[photo.pk] = marker_details
    return HttpResponse(simplejson.dumps(markers), mimetype='application/json')

def json_markers_details(request, photo_pk):
    """
    Returns detailed information about the requested photo. The data returned
    is serialized as JSON.
    """
    if not request.is_ajax():
        raise Http404
    photo = get_object_or_404(Photo, pk=photo_pk)
    # Get the EXIF tags that belongs to the current photo
    displayed_exif_tags = [tag.strip() for tag in config.DISPLAYED_EXIF_TAGS.split('\n')]
    exif_tags = photo.exiftag_set.filter(key__in=displayed_exif_tags)
    sorted_exif_tags = [exif_tags.filter(key=tag).values('key', 'value')[0] for tag in displayed_exif_tags if exif_tags.filter(key=tag).count() > 0]
    marker_details = dict()
    marker_details['et'] = sorted_exif_tags
    marker_details['sm_url'] = get_thumbnail(photo.file, settings.PHOTO_SMALL_SIZE, crop='noop').url
    marker_details['lg_url'] = get_thumbnail(photo.file, settings.PHOTO_LARGE_SIZE, crop='noop').url
    marker_details['srch_qry'] = urllib.urlencode({ 'q': photo.get_location() })
    return HttpResponse(simplejson.dumps(marker_details), mimetype='application/json')

def map(request):
    """
    Displays a map with markers for every photo.
    Hovering over a marker will pop a window with basic informations on the
    photo, and a click on the marker will fill the left side of the page
    with more details. The information displayed on the page is fetched
    asynchronously.
    """
    context = RequestContext(request)
    context.update({ 
                    'DEFAULT_PHOTO': settings.DEFAULT_PHOTO,
                    'PHOTO_SMALL_SIZE': settings.PHOTO_SMALL_SIZE
    })
    return render_to_response('map.html', context)

