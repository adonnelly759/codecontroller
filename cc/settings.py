"""
Django settings for cc project.

Generated by 'django-admin startproject' using Django 3.0.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'lprtu=y9oeo0tmo%$$ov6o38p+4)&o7)#t(43+uzr)hxgxkdwg'

LOGOUT_REDIRECT_URL = '/'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Channels
ASGI_APPLICATION = 'cc.routing.application'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [os.environ.get('REDIS_URL', 'redis://localhost:6379')],
        },
    },
}

# Application definition

INSTALLED_APPS = [
    'django_extensions',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dash',
    'editor',
    'front',
    'utils',
    'channels',
    'notifications.apps.NotificationsConfig',
    'badges',
    'account',
    'activity.apps.ActivityConfig',
    'chat',
    'tinymce',
    'ckeditor',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cc.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'dash.context_processors.notification_count',
                'dash.context_processors.get_five_notifications',
                'dash.context_processors.leaderboardPos',
            ],
        'libraries': {
            'split_answers': 'dash.templatetags.quiz_extras'
            }
        },
    },
]

WSGI_APPLICATION = 'cc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Email Config
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_POST = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'nrcodecontroller@gmail.com'
EMAIL_HOST_PASSWORD = "Easter12"
CKEDITOR_CONFIGS = { 'default': 
                         { 'toolbar': 'Custom', 'height': 500, 'toolbar_Custom': 
                             [ 
                                 ['Styles', 'Format', 'Bold', 'Italic', 'Underline', 'Strike', 'SpellChecker', 'Undo', 'Redo'], 
                                 ['Link', 'Unlink', 'Anchor'], 
                                 ['Image', 'Flash', 'Table', 'HorizontalRule'], 
                                 ['TextColor', 'BGColor'], 
                                 ['Smiley', 'SpecialChar'], 
                                 ['Source'], 
                             ], 
                           }, 'special': 
                    { 'toolbar': 'Special', 'toolbar_Special': 
                            [ 
                             ['Bold'], ['Link'], ['Unlink'], ['Image'], ['CodeSnippet'], 
                            ], 'extraPlugins': 'codesnippet',
                          } 
                     }