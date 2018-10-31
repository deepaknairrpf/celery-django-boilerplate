from .settings import *  # noqa

DEBUG = True


ALLOWED_HOSTS = ["*"]

# Postgres docker container
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}
