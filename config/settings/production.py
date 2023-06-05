from cloudinary_storage.storage import RawMediaCloudinaryStorage

from config.settings.base import *

ALLOWED_HOSTS = [".vercel.app", ".now.sh"]


INSTALLED_APPS += [
    "cloudinary_storage",
    "cloudinary",
]

CLOUDINARY_STORAGE = {
    "CLOUD_NAME": env("CLOUDINARY_CLOUD_NAME"),
    "API_KEY": env("CLOUDINARY_API_KEY"),
    "API_SECRET": env("CLOUDINARY_API_SECRET"),
}

DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"
