import pytest
from rest_framework.reverse import reverse

from articles.tests.factories import ArticleFactory, SubMenuFactory

pytestmark = pytest.mark.django_db


def test_api_correctly_returns_list_of_articles(api_client):
    article_1, article_2 = ArticleFactory.create_batch(2)

    response = api_client.get(
        reverse(
            "articles:articles-list",
        ),
    )
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2

    assert data[0]["code"] == article_1.code
    assert data[0]["language"] == article_1.language
    assert data[0]["menu_display_name"] == article_1.menu_display_name

    assert data[1]["code"] == article_2.code
    assert data[1]["language"] == article_2.language
    assert data[1]["menu_display_name"] == article_2.menu_display_name


def test_api_correctly_returns_article_detail(api_client):
    article = ArticleFactory()

    response = api_client.get(
        reverse(
            "articles:articles-detail",
            kwargs={
                "code": article.code,
            },
        ),
    )
    assert response.status_code == 200
    data = response.json()

    assert data["code"] == article.code
    assert data["language"] == article.language
    assert data["html_content"] == article.html_content


def test_api_correctly_returns_menu(api_client):
    main_article_1, main_article_2 = ArticleFactory.create_batch(2)

    sub_menu_1 = SubMenuFactory()
    sub_article_1, sub_article_2 = ArticleFactory.create_batch(
        2,
        sub_menu=sub_menu_1,
    )
    ArticleFactory(is_menu_visible=False)
    ArticleFactory(language="en")

    response = api_client.get(
        reverse(
            "articles:articles-get-menu",
            kwargs={
                "language": "pl",
            },
        ),
    )
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2

    assert len(data["main_menu"]) == 2
    assert data["main_menu"][0]["code"] == main_article_1.code
    assert data["main_menu"][0]["language"] == main_article_1.language
    assert data["main_menu"][0]["menu_display_name"] == main_article_1.menu_display_name
    assert data["main_menu"][1]["code"] == main_article_2.code
    assert data["main_menu"][1]["language"] == main_article_2.language
    assert data["main_menu"][1]["menu_display_name"] == main_article_2.menu_display_name

    assert len(data[sub_menu_1.menu_display_name]) == 2
    assert data[sub_menu_1.menu_display_name][0]["code"] == sub_article_1.code
    assert data[sub_menu_1.menu_display_name][0]["language"] == sub_article_1.language
    assert (
        data[sub_menu_1.menu_display_name][0]["menu_display_name"]
        == sub_article_1.menu_display_name
    )
    assert data[sub_menu_1.menu_display_name][1]["code"] == sub_article_2.code
    assert data[sub_menu_1.menu_display_name][1]["language"] == sub_article_2.language
    assert (
        data[sub_menu_1.menu_display_name][1]["menu_display_name"]
        == sub_article_2.menu_display_name
    )
