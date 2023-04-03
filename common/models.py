from model_clone.models import CloneModel


class BaseModel(CloneModel):
    class Meta(CloneModel.Meta):
        abstract = True
