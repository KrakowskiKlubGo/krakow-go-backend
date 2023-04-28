"""
Django settings for krakow_go_backend project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
import environ
from pathlib import Path

from rest_captcha.settings import FONT_PATH


env = environ.Env(DEBUG=(bool, False))

BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

SECRET_KEY = env("SECRET_KEY")


DEBUG = env("DJANGO_DEBUG")

ALLOWED_HOSTS = [".vercel.app", ".now.sh"]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]

# Application definition

ADMIN_MODIFICATION_APPS = [
    "jazzmin",
    "model_clone",
]

FILE_STORAGE_APPS = [
    "cloudinary_storage",
    "cloudinary",
]

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "corsheaders",
    "modeltranslation",
    "rest_captcha",
]

KRAKOW_GO_BACKEND_APPS = [
    "common.apps.CommonConfig",
    "tournaments.apps.TournamentsConfig",
    "meetings.apps.MeetingsConfig",
    "sgfs.apps.SgfsConfig",
    "articles.apps.ArticlesConfig",
]

INSTALLED_APPS = (
    THIRD_PARTY_APPS
    + ADMIN_MODIFICATION_APPS
    + DJANGO_APPS
    + FILE_STORAGE_APPS
    + KRAKOW_GO_BACKEND_APPS
)

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.locale.LocaleMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["common/templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env("DB_NAME"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASSWORD"),
        "HOST": env("DB_HOST"),
        "PORT": env("DB_PORT"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "pl"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

gettext = lambda s: s
LANGUAGES = [
    ("pl", gettext("Polish")),
    ("en", gettext("English")),
]
MODELTRANSLATION_DEFAULT_LANGUAGE = "pl"
MODELTRANSLATION_PREPOPULATE_LANGUAGE = "pl"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles_build", "static")


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Jazzmin settings
JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Krakowski Klub Go",
    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "Krakowski Klub Go",
    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "Krakowski Klub Go",
    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "logo.png",
    # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
    "login_logo": "logo.png",
    # Logo to use for login form in dark themes (defaults to login_logo)
    "login_logo_dark": "logo.png",
    # CSS classes that are applied to the logo above
    "site_logo_classes": "img-circle",
    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": None,
    # Welcome text on the login screen
    "welcome_sign": "Panel administracyjny",
    # Copyright on the footer
    "copyright": "Krakowski Klub Go",
    # List of model admins to search from the search bar, search bar omitted if excluded
    # If you want to use a single search field you dont need to use a list, you can use a simple string
    "search_model": [],
    # Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
    "user_avatar": None,
    # Top Menu #
    "topmenu_links": [],
    # Side Menu #
    "show_sidebar": True,
    # Whether to aut expand the menu
    "navigation_expanded": True,
    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": [],
    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": [],
    # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    "order_with_respect_to": [
        "auth",
    ],
    # Custom links to append to app groups, keyed on app name
    "custom_links": {
        "team": [
            {
                # Any Name you like
                "name": "Make Messages",
                # url name e.g `admin:index`, relative urls e.g `/admin/index` or absolute urls e.g `https://domain.com/admin/index`
                "url": "make_messages",
                # any font-awesome icon, see list here https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2 (optional)
                "icon": "fas fa-comments",
                # a list of permissions the user must have to see this link (optional)
                "permissions": ["books.view_book"],
            }
        ]
    },
    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    # for the full list of 5.13.0 free icon classes
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    "related_modal_active": False,
    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": None,
    "custom_js": None,
    # Whether to link font from fonts.googleapis.com (use custom_css to supply font otherwise)
    "use_google_fonts_cdn": True,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": True,
    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
    },
    # Add a language dropdown into the admin
    "language_chooser": False,
}

# MEDIA
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
# https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = "/media/"
MAX_UPLOAD_FILE_SIZE = 250000000
DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"

CLOUDINARY_STORAGE = {
    "CLOUD_NAME": env("CLOUDINARY_CLOUD_NAME"),
    "API_KEY": env("CLOUDINARY_API_KEY"),
    "API_SECRET": env("CLOUDINARY_API_SECRET"),
}


# CACHE
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "rest-captcha",
        "MAX_ENTRIES": 10000,
    }
}

# CAPTCHA
REST_CAPTCHA = {
    "CAPTCHA_CACHE": "default",
    "CAPTCHA_TIMEOUT": 300,  # 5 minutes
    "CAPTCHA_LENGTH": 4,
    "CAPTCHA_FONT_SIZE": 22,
    "CAPTCHA_IMAGE_SIZE": (90, 40),
    "CAPTCHA_LETTER_ROTATION": (-35, 35),
    "CAPTCHA_FOREGROUND_COLOR": "#001100",
    "CAPTCHA_BACKGROUND_COLOR": "#ffffff",
    "CAPTCHA_FONT_PATH": FONT_PATH,
    "CAPTCHA_CACHE_KEY": "rest_captcha_{key}.{version}",
    "FILTER_FUNCTION": "rest_captcha.captcha.filter_default",
    "NOISE_FUNCTION": "rest_captcha.captcha.noise_default",
}
