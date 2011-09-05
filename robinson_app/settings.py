import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Montreal'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# This makes it possible to read the EXIF metadata from small files 
# in django-robinson since otherwise it would try to read them before
# being physically copied to disk and would fail
FILE_UPLOAD_MAX_MEMORY_SIZE = 1

FILE_UPLOAD_PERMISSIONS = 0600

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.dirname(os.path.realpath( __file__ )) + '/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = ''

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',   # Add the request to the context
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.media',     # Add MEDIA_URL to the context
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'robinson_app.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.dirname(os.path.realpath( __file__ )) + '/templates',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    
    'constance',
    'constance.backends.database',
    'django_extensions',
    'gmapi',
    'robinson',
    'sorl.thumbnail',
    'south',
    'tagging',
)

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'
CONSTANCE_CONFIG = {
    'DISPLAYED_EXIF_TAGS': (
        'Exif.Photo.ExposureTime\nExif.Photo.FNumber\nExif.Photo.ISOSpeedRatings\nExif.Photo.FocalLength\nExif.Photo.ExposureProgram\nExif.Image.Model',
        'Ordered list of EXIF tags to display. One EXIF tag per line.',
    ),
    'GA_ID': (
        '',
        'Google Analytics web property ID (ie. UA-9999999-1).',
    ),
}

# Use GraphicsMagick instead of the default PIL
THUMBNAIL_ENGINE = 'sorl.thumbnail.engines.pgmagick_engine.Engine'

DEFAULT_PHOTO = MEDIA_ROOT + 'images/johnny_automatic_man_with_a_camera.svg'
PHOTO_THUMBNAIL_SIZE = '125x125'
PHOTO_SMALL_SIZE = '250x250'
PHOTO_LARGE_SIZE = '1280x1280'

# Maximum distance (meters) between photos to be considered a cluster
PHOTO_CLUSTER_MAXIMUM_DISTANCE = 5

