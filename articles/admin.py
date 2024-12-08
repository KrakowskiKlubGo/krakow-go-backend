from django.contrib import admin
from django.db.models import TextField

from articles.models import Article, ArticleImage
from common.admin import CustomTextFieldWidget


class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    extra = 0
    fields = ("image",)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    formfield_overrides = {TextField: {"widget": CustomTextFieldWidget}}
    list_display = (
        "code",
        "language",
        "add_to_menu",
        "menu_order",
    )
    inlines = [ArticleImageInline]


class ArticleInline(admin.TabularInline):
    model = Article
    extra = 0
    fields = "language"
    readonly_fields = "language"

    def has_add_permission(self, request, obj):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
