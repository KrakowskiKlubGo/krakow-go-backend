from django_filters import FilterSet

from meetings.models import Meeting


class MeetingFilter(FilterSet):
    class Meta:
        model = Meeting
        fields = {"date": ["exact", "lt", "gt"]}
