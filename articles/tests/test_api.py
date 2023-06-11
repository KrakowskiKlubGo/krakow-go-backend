import pytest
from rest_framework.reverse import reverse

from articles.tests.factories import ArticleFactory

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

    assert data[1]["code"] == article_2.code
    assert data[1]["language"] == article_2.language


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
