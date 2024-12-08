from django.conf.urls.i18n import i18n_patterns
from django.urls import path
from django_distill import distill_path

from articles.models import Article
from meetings.models import Meeting
from web_pages.views import HomeView, TournamentsView, ArticleView, EventView


def get_articles():
    for article in Article.objects.all():
        yield {"code": article.code}


def get_events():
    for event in Meeting.objects.filter(is_active=True):
        yield {"code": event.code}


patterns = [
    path("", HomeView.as_view(), name="index"),
    path("turnieje/", TournamentsView.as_view(), name="tournaments"),
    path("p/<slug:code>/", ArticleView.as_view(), name="article"),
    path("wydarzenia/<slug:code>/", EventView.as_view(), name="event"),
]

dynamic_patterns = i18n_patterns(*patterns, prefix_default_language=False)

static_patterns = i18n_patterns(
    distill_path(
        "",
        HomeView.as_view(),
        name="index-static",
        distill_func=lambda: None,
    ),
    distill_path(
        "turnieje/",
        TournamentsView.as_view(),
        name="tournaments-static",
        distill_func=lambda: None,
    ),
    distill_path(
        "p/<slug:code>/",
        ArticleView.as_view(),
        name="article-static",
        distill_func=get_articles,
    ),
    distill_path(
        "wydarzenia/<slug:code>/",
        EventView.as_view(),
        name="event-static",
        distill_func=get_events,
    ),
    prefix_default_language=False,
)

urlpatterns = dynamic_patterns + static_patterns
