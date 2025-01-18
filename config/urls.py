"""krakow_go_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from web_pages import urls as web_urls

urlpatterns = (
    [
        path("admin/", admin.site.urls),
        # trigger_github_action view
        path(
            "command/",
            include(("common.urls", "common"), namespace="common"),
        ),
        # API
        path(
            "api/",
            include(("tournaments.urls", "tournaments"), namespace="tournaments"),
        ),
        path("api/", include(("meetings.urls", "meetings"), namespace="meetings")),
        path("api/", include(("articles.urls", "articles"), namespace="articles")),
        path("api/", include(("sgfs.urls", "sgfs"), namespace="sgfs")),
        path("api/captcha/", include("rest_captcha.urls")),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + web_urls.urlpatterns
)

if settings.DEBUG:
    urlpatterns += [path("__reload__/", include("django_browser_reload.urls"))]


if settings.DEFAULT_FILE_STORAGE == "django.core.files.storage.FileSystemStorage":
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
