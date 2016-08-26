# Copyright 2015 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Django settings for project_name project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qgw!j*bpxo7g&o1ux-(2ph818ojfj(3c#-#*_8r^8&hq5jg$3@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# when using "Services", the host turns out to be:
# {{GAE_MODULE_NAME}}-dot-{{GAE_APPENGINE_HOSTNAME}}
ALLOWED_HOSTS = ['*', os.environ.get('GAE_APPENGINE_HOSTNAME', '')]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'helloworld'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'helloworld.middleware.LiveDebuggerTestMiddleware',
)

ROOT_URLCONF = 'project_name.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'project_name.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'testing',
        'STORAGE_ENGINE': 'INNODB',
        'USER': 'root',
        'OPTIONS': {
            'unix_socket': '/cloudsql/imtapps-cloudsql:internal-apps',
        }
    }
}

MEMCACHED_LOCATION = "{memcache_addr}:{memcache_port}".format(
    memcache_addr=os.environ.get('MEMCACHE_PORT_11211_TCP_ADDR', 'localhost'),
    memcache_port=os.environ.get('MEMCACHE_PORT_11211_TCP_PORT', 11211)
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'TIMEOUT': 60*15,  # 15 minutes
        'LOCATION': MEMCACHED_LOCATION,
    },
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")
# STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'


# http://stackoverflow.com/questions/36941184/error-reporting-with-app-engine-flexible-environment/37071628#37071628
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        }
    },
    'formatters': {
        'gcp_json': {
            '()': 'helloworld.gcp_logger.GCPJsonFormatter',
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/var/log/app_engine/custom_logs/errors.json',
            'formatter': 'gcp_json',
        },
    },
    'loggers': {
        'django.request': {
            'filters': ['require_debug_false'],
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}
