from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-p-t+o45im!_+t==fpnc!!!r@yp((s!6=%*#1t4oeh3q$@d6e#*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1", "web-production-8f08.up.railway.app", "www.voltageitlabs.com", "voltageitlabs.com"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "whitenoise.runserver_nostatic",

    # Custom apps
    'main_app.apps.MainAppConfig',
    'accounts.apps.AccountsConfig',
    'tailwind',
    'voltage_tailwind',
    # 'django_browser_reload',
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
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # "django_browser_reload.middleware.BrowserReloadMiddleware",
]

# Point the user to custom user model created.
AUTH_USER_MODEL = "accounts.CustomUser"

ROOT_URLCONF = 'voltage_labs.urls'

# Set up template rendering
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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

WSGI_APPLICATION = 'voltage_labs.wsgi.application'


# Database

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "railway",
        "USER": "postgres",
        "PASSWORD": "B0BBahPxcLDl1vzqg13X",
        "HOST": "containers-us-west-190.railway.app",
        "PORT": "7389",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Set up static file configurations
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

# Set up static in deployment.

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Add a path for uploaded files in case of any.
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")

# Handle static file in production using whitenoise.
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

# Tailwind configurations.
TAILWIND_APP_NAME = 'voltage_tailwind'
INTERNAL_IPS = [
    "127.0.0.1",
]

# NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"

# Email Configurations and Sending.
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'voltageitlabs@gmail.com'
EMAIL_HOST_PASSWORD = 'rsvinerizghwrhlj'
YOUR_INBOX_EMAIL = 'voltageitlabs@gmail.com'

CSRF_TRUSTED_ORIGINS = ['https://web-production-8f08.up.railway.app', 'https://www.voltageitlabs.com']