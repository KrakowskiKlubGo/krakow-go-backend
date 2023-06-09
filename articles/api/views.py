from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from articles.api.serializers import ArticleListSerializer, ArticleSerializer
from articles.models import Article
from articles.service import ArticlesMenuTreeBuilder


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_field = "code"
    queryset = Article.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return ArticleListSerializer
        return ArticleSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = get_object_or_404(
            Article.objects.filter(code=kwargs["code"], language=request.LANGUAGE_CODE)
        )
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @action(
        detail=False,
        methods=["get"],
        url_path="menu/(?P<language>[a-z]{2})",
    )
    def get_menu(self, request, language):
        """
        Return a tree of articles grouped by submenu.
        """
        articles = Article.objects.filter(is_menu_visible=True, language=language)
        menu = ArticlesMenuTreeBuilder(articles).build()
        return Response(
            menu,
            status=status.HTTP_200_OK,
        )
