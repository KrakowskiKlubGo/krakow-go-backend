from model_clone import CloneModelAdminMixin
from modeltranslation.admin import TranslationAdmin


class CloneTranslationModelAdmin(CloneModelAdminMixin, TranslationAdmin):
    pass
