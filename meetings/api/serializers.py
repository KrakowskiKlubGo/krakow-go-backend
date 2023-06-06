from rest_framework import serializers

from meetings.models import Meeting


class BaseMeetingSerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField()
    start_time = serializers.TimeField(format="%H:%M")
    end_time = serializers.TimeField(format="%H:%M")

    class Meta:
        model = Meeting

    def get_date(self, obj):
        if hasattr(obj, "onetimemeeting"):
            return obj.onetimemeeting.date.strftime("%Y-%m-%d")
        else:
            return obj.recurringmeeting.date.strftime("%Y-%m-%d")


class MeetingListSerializer(BaseMeetingSerializer):
    class Meta:
        model = Meeting
        fields = ("code", "name", "date", "start_time", "end_time", "address")


class MeetingSerializer(BaseMeetingSerializer):
    class Meta:
        model = Meeting
        fields = (
            "name",
            "date",
            "start_time",
            "end_time",
            "address",
            "address_map_link",
            "description",
        )
