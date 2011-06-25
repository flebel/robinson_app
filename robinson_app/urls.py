from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^markers.json$', 'robinson_app.views.json_markers'),
    (r'^markers/(?P<photo_pk>\d*).json$', 'robinson_app.views.json_markers_details'),
    (r'^$', 'robinson_app.views.map'),
)

# Serve static content from Django only when in DEBUG
if settings.DEBUG:
    media_url = settings.MEDIA_URL
    if len(media_url) > 1 and media_url.startswith('/'):
        media_url = media_url[1:]
    urlpatterns = patterns('',
        (r'', include('gmapi.urls.media')),
        (r'^%s(?P<path>.*)$' % media_url, 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT }),
    ) + urlpatterns

