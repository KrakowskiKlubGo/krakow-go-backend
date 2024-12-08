from model_clone.models import CloneModel


class BaseModel(CloneModel):
    class Meta(CloneModel.Meta):
        abstract = True


class DummyModel(BaseModel):
    """
    Dummy model so the common app is taken into consideration by Jazzmin
    to show the models in the admin panel under common.
    """

    pass
