from django.urls import reverse
from django.urls import reverse
from django.utils.translation import gettext as _, get_language
from django.views.generic import TemplateView, DetailView

from articles.models import Article
from meetings.models import Meeting
from tournaments.models import TournamentInfo


class BaseViewMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        menu_articles = Article.objects.filter(
            add_to_menu=True, language=get_language()
        ).order_by("menu_order")
        context["menu"] = [{"name": _("TURNIEJE"), "url": reverse("tournaments")},] + [
            {
                "name": article.title,
                "url": reverse("article", kwargs={"code": article.code}),
            }
            for article in menu_articles
        ]
        return context


class HomeView(BaseViewMixin, TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tournaments"] = TournamentInfo.objects.upcoming()
        context["meetings"] = Meeting.objects.upcoming()
        return context


class TournamentsView(BaseViewMixin, TemplateView):
    template_name = "tournaments.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["past_tournaments"] = TournamentInfo.objects.past()
        context["upcoming_tournaments"] = TournamentInfo.objects.upcoming()
        return context


class ArticleView(BaseViewMixin, DetailView):
    template_name = "article.html"
    slug_url_kwarg = "code"
    slug_field = "code"

    def get_queryset(self):
        return Article.objects.all()


class EventView(BaseViewMixin, DetailView):
    template_name = "event.html"
    slug_url_kwarg = "code"
    slug_field = "code"

    def get_queryset(self):
        return Meeting.objects.filter(is_active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
