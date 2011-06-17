from constance import config
from django import forms
from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string
from gmapi import maps
from gmapi.forms.widgets import GoogleMap
from robinson.models import *
from sorl.thumbnail import get_thumbnail
import urllib


# Center the map at the geographical center of North America
MAP_CENTER = maps.LatLng(48.354479, -99.998135)

class MapForm(forms.Form):
    map = forms.Field(widget=GoogleMap(attrs={ 'height': 640, 'width': 800 }))

def map(request):
    """
    Displays a map with markers for every photo.
    Hovering over a marker will pop a window with basic informations on the
    photo, and a click on the marker will fill the left side of the page
    with more details.
    """
    # Create the map with its settings
    gmap = maps.Map(opts = {
        'center': MAP_CENTER,
        'mapTypeId': maps.MapTypeId.HYBRID,
        'keyboardShortcuts': False,
        'mapTypeControlOptions': {
             'style': maps.MapTypeControlStyle.DROPDOWN_MENU
        },
        'scaleControl': True,
        'zoom': 3,
    })
    # Add the markers for every photo
    for photo in Photo.objects.all():
        # Skip the current photo if it is not valid, i.e. was automatically
        # imported and no geolocation information has been set yet
        if not photo.is_valid():
            continue
        marker = maps.Marker(opts = {
            'map': gmap,
            'position': maps.LatLng(photo.latitude, photo.longitude),
        })
        maps.event.addListener(marker, 'click', 'robinson.markerClick')
        maps.event.addListener(marker, 'mouseover', 'robinson.markerOver')
        maps.event.addListener(marker, 'mouseout', 'robinson.markerOut')
        # Get the EXIF tags that belongs to the current photo
        displayed_exif_tags = [tag.strip() for tag in config.DISPLAYED_EXIF_TAGS.split('\n')]
        exif_tags = photo.exiftag_set.filter(key__in=displayed_exif_tags)
        sorted_exif_tags = [exif_tags.filter(key=tag)[0] for tag in displayed_exif_tags if exif_tags.filter(key=tag).count() > 0]
        # Use the latest EXIF tag as the date at which the picture was taken
        date_taken = photo.exiftag_set.filter(key='Exif.Image.DateTime').latest('value').value
        search_url_query = urllib.urlencode({ 'q': photo.get_location() })
        context = {
            'PHOTO_LARGE_SIZE': settings.PHOTO_LARGE_SIZE,
            'PHOTO_SMALL_SIZE': settings.PHOTO_SMALL_SIZE,
            'PHOTO_THUMBNAIL_SIZE': settings.PHOTO_THUMBNAIL_SIZE,
            'date_taken': date_taken,
            'exif_tags': sorted_exif_tags,
            'photo': photo,
            'search_url_query': search_url_query
        }
        details_content = render_to_string('marker_details.html', context)
        window_content = render_to_string('marker_window.html', context)
        info = maps.InfoWindow({
            'content': window_content,
            'details_content': details_content,
            'disableAutoPan': True
        })
        info.open(gmap, marker)
    context = RequestContext(request)
    context.update({ 
                    'DEFAULT_PHOTO': settings.DEFAULT_PHOTO,
                    'PHOTO_SMALL_SIZE': settings.PHOTO_SMALL_SIZE,
                    'form': MapForm(initial={ 'map': gmap })
    })
    return render_to_response('map.html', context)

