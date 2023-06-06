from typing import List

from articles.api.serializers import ArticleListSerializer


class ArticlesMenuTreeBuilder:
    def __init__(self, articles):
        self.articles = articles

    def build(self):
        """
        Build a tree of provided articles. Only submenus of provided articles are
        included. Articles without submenu are included in main_menu.
        """
        menu = {
            "main_menu": [
                ArticleListSerializer(article).data
                for article in self.articles
                if article.sub_menu is None
            ],
        }
        for article in self.articles:
            if article.sub_menu is not None:
                submenu = article.sub_menu.menu_display_name
                if submenu not in menu:
                    menu[submenu] = []
                menu[submenu].append(ArticleListSerializer(article).data)

        return menu
