from config.settings.base import *


ALLOWED_HOSTS = ["127.0.0.1"]

DEBUG = True

DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
