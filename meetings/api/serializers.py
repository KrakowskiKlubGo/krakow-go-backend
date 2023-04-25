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
        fields = ("id", "name", "date", "start_time", "end_time", "address")


class MeetingSerializer(BaseMeetingSerializer):
    participants_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Meeting
        fields = (
            "name",
            "date",
            "start_time",
            "end_time",
            "participants_count",
            "address",
            "address_map_link",
            "description",
        )


class MeetingParticipantCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, default="Anonim")
    meeting_id = serializers.PrimaryKeyRelatedField(queryset=Meeting.objects.all())
