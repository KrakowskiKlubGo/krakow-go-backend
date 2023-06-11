import factory
from factory.django import DjangoModelFactory

from articles.models import Article


class ArticleFactory(DjangoModelFactory):
    class Meta:
        model = Article

    code = factory.Sequence(lambda n: f"article-{n}")
    language = "pl"
    html_content = factory.Faker("text")
