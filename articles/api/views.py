from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from articles.api.serializers import ArticleListSerializer, ArticleSerializer
from articles.models import Article


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
