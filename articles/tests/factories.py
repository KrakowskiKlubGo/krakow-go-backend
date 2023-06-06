import factory
from factory.django import DjangoModelFactory

from articles.models import Article, SubMenu


class ArticleFactory(DjangoModelFactory):
    class Meta:
        model = Article

    code = factory.Sequence(lambda n: f"article-{n}")
    menu_display_name = factory.Faker("word")
    language = "pl"
    html_content = factory.Faker("text")
    is_menu_visible = True


class SubMenuFactory(DjangoModelFactory):
    class Meta:
        model = SubMenu

    menu_display_name = factory.Faker("word")
    language = "pl"
