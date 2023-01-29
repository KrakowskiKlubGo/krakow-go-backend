from rest_framework import viewsets

from articles.api.serializers import ArticleListSerializer, ArticleSerializer
from articles.models import Article


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return ArticleListSerializer
        return ArticleSerializer
