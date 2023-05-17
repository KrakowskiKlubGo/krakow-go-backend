from django.contrib import admin
from django.db.models import TextField

from articles.models import Article, SubMenu
from common.admin import CustomTextFieldWidget


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    formfield_overrides = {TextField: {"widget": CustomTextFieldWidget}}
    list_display = ("code", "language", "is_draft")


class ArticleInline(admin.TabularInline):
    model = Article
    extra = 0
    fields = ("menu_display_name", "language")
    readonly_fields = ("menu_display_name", "language")

    def has_add_permission(self, request, obj):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(SubMenu)
class SubMenuAdmin(admin.ModelAdmin):
    list_display = ("menu_display_name", "language")
    inlines = [ArticleInline]
