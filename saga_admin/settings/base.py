# Django settings for project project.
from unipath import Path
from os import environ
from django.core.exceptions import ImproperlyConfigured


def get_env_setting(setting, default=None):
    """ Get the environment setting or return exception """
    try:
        var = environ.get(setting, default) if default else environ[setting]
        return var
    except KeyError:
        error_msg = "Set the %s env variable" % setting
        raise ImproperlyConfigured(error_msg)

PROJECT_ROOT = Path(__file__).ancestor(3)

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
     ('Ben Beecher', 'BenBeecher@gmail.com'),
)

MANAGERS = ADMINS


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    PROJECT_ROOT.child("static_source"),# An absolute path: /foo/bar/baz.py
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = "+f133qe%d0hpv##b33is^js6yhlx40%lju)=+0+uz%q4-b#1#y"

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = ("django.contrib.auth.context_processors.auth",
                               "django.core.context_processors.debug",
                               "django.core.context_processors.request",
                               "django.core.context_processors.i18n",
                               "django.core.context_processors.media",
                               "django.core.context_processors.static",
                               "django.core.context_processors.tz",
                               "django.contrib.messages.context_processors.messages",
                               "django.core.context_processors.media",
                               "app.context_processors.settings",
                               'social.apps.django_app.context_processors.backends',
                               'social.apps.django_app.context_processors.login_redirect',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "social.apps.django_app.middleware.SocialAuthExceptionMiddleware",
)

ROOT_URLCONF = 'saga_admin.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'saga_admin.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    PROJECT_ROOT.child('templates')
)

INSTALLED_APPS = (
    # Grapelli tools
    'grappelli.dashboard',
    'grappelli',
    'filebrowser',
    'reversion',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'annoying',
    'django_extensions',
    'model_utils',
    'south',
    'pipeline',
    'easy_thumbnails',
    'django_nose',
    'registration',
    'payments',
    'manifesto',
    'social.apps.django_app.default',
    'smuggler',
    'app',
    'account',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'account.backends.UserAuthBackend',
    'social.backends.facebook.FacebookOAuth2',
)

AUTH_USER_MODEL = 'account.User'
LOGIN_REDIRECT_URL = "/"
LOGIN_URL = "/account/login"
LOGOUT_URL = "/account/logout"

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# Tell nose to measure coverage on the 'app' and 'account' apps
NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=app,account',
]

import scss
scss.config.PROJECT_ROOT = PROJECT_ROOT
scss.config.STATIC_URL = STATIC_URL

ALLOWED_HOSTS = [
    "localhost"
    ".herokuapp.com"
]

DEFAULT_FROM_EMAIL = "hello@saga_admin.com"
SERVER_EMAIL = "error@saga_admin.com"
from saga_admin.settings.app import *


SOUTH_TESTS_MIGRATE = False

#for easy thumbnails
SOUTH_MIGRATION_MODULES = {
    'easy_thumbnails': 'easy_thumbnails.south_migrations',
}


GRAPPELLI_ADMIN_TITLE = 'saga_admin'
