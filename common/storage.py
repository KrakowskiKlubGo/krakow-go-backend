from cloudinary_storage.storage import RawMediaCloudinaryStorage
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.db.models.fields.files import FieldFile


class RawFieldFile(FieldFile):
    def __init__(self, instance, field, name):
        super(RawFieldFile, self).__init__(instance, field, name)
        if (
            settings.DEFAULT_FILE_STORAGE
            == "cloudinary_storage.storage.MediaCloudinaryStorage"
        ):
            self.storage = RawMediaCloudinaryStorage()
        else:
            self.storage = FileSystemStorage()


class RawFileField(models.FileField):
    """
    Allows to use cloudinary storage or local storage for text files depending
    on DEFAULT_FILE_STORAGE setting.
    """

    attr_class = RawFieldFile

    def pre_save(self, model_instance, add):
        file = super(RawFileField, self).pre_save(model_instance, add)
        if file and not file._committed:
            # Commit the file to storage prior to saving the model
            file.save(file.name, file.file, save=False)
        return file
