from .settings import *

DEBUG = False
DEFAULT_FILE_STORAGE = 'storages.backends.azure_storage.AzureStorage'
STATICFILES_STORAGE = 'storages.backends.azure_storage.AzureStorage'
AZURE_ACCOUNT_NAME = os.getenv('AZ_STORAGE_ACCOUNT_NAME')
AZURE_CONTAINER = os.getenv('AZ_STORAGE_CONTAINER')
AZURE_ACCOUNT_KEY = os.getenv('AZ_STORAGE_KEY')

AZ_GROUP='wshar_rg_Linux_australiaeast'
AZ_LOCATION='australiaeast'

APP_SERVICE_APP_NAME='apiarydev'

POSTGRES_SERVER_NAME='django.db.backends.postgresql'
POSTGRES_ADMIN_USER='qgvvzgpx'
POSTGRES_ADMIN_PASSWORD='lJn3plV_Qp4KA-8woHA1y0yLxEjGQmif'

POSTGRES_HOST='rosie.db.elephantsql.com'

APP_DB_NAME='qgvvzgpx'

DJANGO_SETTINGS_MODULE='apiary_project.azure'

AZ_STORAGE_ACCOUNT_NAME='apiarydevstorage'
AZ_STORAGE_KEY='n2fI+fanSIHjlLOltt/mqMviq1S9c9fJ7g+g8/r3b4eLzuRLWiB50JE46IBy2yAqh38N35daN5cpF3ET8tc+HQ=='
AZ_STORAGE_CONTAINER='apiarydevstoragecontainer'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('APP_DB_NAME'),
        'USER': os.getenv('POSTGRES_ADMIN_USER'),
        'PASSWORD': os.getenv('POSTGRES_ADMIN_PASSWORD'),
        'HOST': os.getenv('POSTGRES_HOST'),
        'PORT': '5432',
        'OPTIONS': {'sslmode': 'require'},
    }
}

