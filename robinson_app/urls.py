from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markers.json$', 'robinson_app.views.json_markers'),
    url(r'^markers/(?P<photo_pk>\d*).json$', 'robinson_app.views.json_markers_details'),
    url(r'^photo/(?P<photo_pk>\d*)/$', 'robinson_app.views.photo'),
    url(r'^$', 'robinson_app.views.map'),
]

# Serve static content from Django only when in DEBUG
if settings.DEBUG:
    media_url = settings.MEDIA_URL
    if len(media_url) > 1 and media_url.startswith('/'):
        media_url = media_url[1:]
    urlpatterns.extend([
        url(r'', include('gmapi.urls.media')),
        url(r'^%s(?P<path>.*)$' % media_url, 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT }),
    ])

