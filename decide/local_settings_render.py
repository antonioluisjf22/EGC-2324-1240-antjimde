# Render deployment settings
import os
import dj_database_url

# Allow all hosts on Render (with CSRF configuration)
ALLOWED_HOSTS = ["decide-render.onrender.com", "localhost", "127.0.0.1"]

# Modules
MODULES = [
    'authentication',
    'base',
    'booth',
    'census',
    'mixnet',
    'postproc',
    'store',
    'visualizer',
    'voting',
]

# Database configuration from environment
DATABASE_URL = os.environ.get('DATABASE_URL')
if DATABASE_URL:
    DATABASES = {
        'default': dj_database_url.config(default=DATABASE_URL, conn_max_age=600)
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'decide',
            'USER': 'decide',
            'PASSWORD': os.environ.get('DB_PASSWORD', 'decide'),
            'HOST': os.environ.get('DB_HOST', 'localhost'),
            'PORT': '5432',
        }
    }

# API configuration
BASEURL = os.environ.get('BASEURL', 'https://decide-render.onrender.com')
APIS = {
    'authentication': BASEURL,
    'base': BASEURL,
    'booth': BASEURL,
    'census': BASEURL,
    'mixnet': BASEURL,
    'postproc': BASEURL,
    'store': BASEURL,
    'visualizer': BASEURL,
    'voting': BASEURL,
}

# Security settings
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'staticfiles')

# CORS settings
CORS_ALLOWED_ORIGINS = [
    "https://decide-render.onrender.com",
    "https://www.decide-render.onrender.com",
]

# Key bits
KEYBITS = 256

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}
