from django.contrib import admin

from sgfs.models import Sgf


@admin.register(Sgf)
class SgfAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "timestamp")
