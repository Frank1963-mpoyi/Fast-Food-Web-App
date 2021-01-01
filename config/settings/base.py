
import os
# import configparser
# from pathlib     import Path
from decouple   import config # is working with secret key
import django_heroku




# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
            )
        )
    )



SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['ruthmitongorestaurant.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    #Project Apps
    'food',
    'AjaxProject',
    'crispy_forms',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    
    
    # Whitenoise
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # i put second bcz it must run first before others
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Whitenoise
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'



#crispy
CRISPY_TEMPLATE_PACK = 'bootstrap4'




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


TIME_ZONE       = 'Africa/Johannesburg'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/




STATIC_URL = '/static/'
STATIC_ROOT= os.path.join(BASE_DIR, 'assets/static')

STATICFILES_DIRS =[
    os.path.join(BASE_DIR, 'static')
]


MEDIA_URL='/media/' 
MEDIA_ROOT= os.path.join(BASE_DIR, 'assets/static/media')# for production 

#CRISPY_TEMPLATE_PACK ='bootstrap4'
#LOGIN_REDIRECT_URL = 'home_view' 
#LOGIN_URL ='login' 


# Internal Ip for Debug tool bar
# INTERNAL_IPS = ['127.0.0.1']
# if not DEBUG:
#     EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#     EMAIL_HOST_USER = 'frankmpoyi63@gmail.com' 
#     EMAIL_HOST = 'smtp.gmail.com'
#     EMAIL_PORT = 587
#     EMAIL_USE_TLS = True
#     EMAIL_HOST_PASSWORD = 'Paulin63@mpoyi' 

# else:
#     EMAIL_BACKEND = (
#         "django.core.mail.backends.console.EmailBackend"
#     )



#white Noise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

django_heroku.settings(locals())# need to import this package
