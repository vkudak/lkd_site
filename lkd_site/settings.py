"""
Django settings for lkd_site project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# BASE_ABS_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
# BASE_ABS_DIR = os.path.abspath(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'w&m8d)nma*m^a_bs&g5df3s*4tb4!+ct9ot2og91f446_gx^j1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'jurnal',
    'tinymce',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'lkd_site.urls'

WSGI_APPLICATION = 'lkd_site.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        # Postgress
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # 'NAME': 'vkudak_db', # Or path to database file if using sqlite3.
        # 'USER': 'vkudak_dbuser',
        # 'PASSWORD': 'post_pass',
        # 'HOST': 'localhost',   # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        # 'PORT': '', # Set to empty string for default.
        # Sqlite
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

MEDIA_ROOT = '/home/vkudak/python/Django/lkd_site/Observations'
#os.path.join(BASE_DIR, '/Observations')

MEDIA_URL = '/Observations/'
# '/Files/'
LOGIN_URL = '/auth.html'

### ---- tinyMCE ----####
TINYMCE_JS_URL = os.path.join(STATIC_URL, 'js/tiny_mce/tiny_mce.js')
TINYMCE_JS_ROOT = os.path.join(STATIC_URL, "js/tiny_mce")
TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table, paste, searchreplace",
    'theme': "advanced",
    # 'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
}
TINYMCE_SPELLCHECKER = False
TINYMCE_COMPRESSOR = False