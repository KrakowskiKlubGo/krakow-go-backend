from django.urls import path

from common.views import trigger_github_action

urlpatterns = [
    # trigger_github_action
    path("github-action/", trigger_github_action, name="trigger_github_action")
]
