from        .base               import *
import      dj_database_url
from        decouple            import          config




DEBUG               = config('DEBUG')

ALLOWED_HOSTS       = ['127.0.0.1', '']


DATABASES['default'] =  dj_database_url.config()








MIDDLEWARE += [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]



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




BASE_PATH       = os.path.join(BASE_DIR)
APP_STATIC      = 'restaurant/static/'

STATIC_URL      = '/static/'
STATIC_ROOT     = os.path.join(BASE_PATH, APP_STATIC)


MEDIA_URL       = '/media/'
MEDIA_ROOT      = os.path.join(BASE_PATH, f'{APP_STATIC}/media')



CORPS_REPLACE_HTTPS_REFERER     = True
HOST_SCHEME                     = "https://"
SECURE_PROXY_SSL_HEADER         = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT             = True
SESSION_COOKIE_SECURE           = True
CSRF_COOKIE_SECURE              = True
SECURE_HSTS_INCLUDE_SUBDOMAINS  = True
SECURE_HSTS_SECONDS             = 1000000
SECURE_FRAME_DENY               = True



STATICFILES_STORAGE             = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


prod_db                          =  dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)

ENVIRONMENT = 'PRODUCTION'

print("\n")
print("DEBUG        = ", DEBUG      )
print("MODE         = ", ENVIRONMENT)
print("STATIC_ROOT  = ", STATIC_ROOT)
print("MEDIA_ROOT   = ", MEDIA_ROOT )
print("\n")

# Note : dont forget to include production in wsgi