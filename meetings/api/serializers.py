from rest_framework import serializers

from meetings.models import Meeting


class MeetingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = ("id", "name", "date", "start_time", "end_time", "address")


class MeetingSerializer(serializers.ModelSerializer):
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
