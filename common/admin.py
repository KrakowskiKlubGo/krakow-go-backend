from django_ace import AceWidget
from model_clone import CloneModelAdminMixin
from modeltranslation.admin import TranslationAdmin


class CustomTextFieldWidget(AceWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, mode="html", height="700px", width="800px", **kwargs)


class CloneTranslationModelAdmin(CloneModelAdminMixin, TranslationAdmin):
    pass
