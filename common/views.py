import requests
from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect


def trigger_github_action(request):
    if not request.user.is_superuser:
        messages.error(
            request, "You do not have permission to trigger a GitHub action."
        )
        return redirect("admin:index")

    if request.method == "GET":
        # check if any workflow runs are in progress
        response = requests.get(
            "https://api.github.com/repos/KrakowskiKlubGo/krakow-go-backend/actions/runs?status=in_progress",
            headers={
                "Accept": "application/vnd.github.v3+json",
                "Authorization": f"token {settings.GITHUB_ACCESS_TOKEN}",
            },
        )
        if response.status_code != 200:
            messages.error(
                request, "Failed to check if any workflow runs are in progress."
            )
            return redirect("admin:index")
        else:
            data = response.json()
            if data["total_count"] > 0:
                messages.error(request, "There are workflow runs in progress.")
                return redirect("admin:index")

        # Trigger a GitHub action by making a POST request to the GitHub API
        # with the appropriate payload
        response = requests.post(
            "https://api.github.com/repos/KrakowskiKlubGo/krakow-go-backend/actions/workflows/push_ftp.yml/dispatches",
            headers={
                "Accept": "application/vnd.github.v3+json",
                "Authorization": f"token {settings.GITHUB_ACCESS_TOKEN}",
            },
            json={
                "ref": "main",
            },
        )
        if response.status_code == 204:
            messages.success(request, "GitHub action triggered successfully.")
        else:
            messages.error(request, "Failed to trigger GitHub action.")

        return redirect("admin:index")
