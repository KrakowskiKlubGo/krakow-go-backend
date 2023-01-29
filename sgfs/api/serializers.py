from rest_framework import serializers

from sgfs.models import Sgf


class SgfListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sgf
        fields = (
            "id",
            "name",
            "type",
        )


class SgfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sgf
        fields = (
            "id",
            "name",
            "type",
            "sgf_file",
        )
