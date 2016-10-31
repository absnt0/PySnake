from rest_framework import serializers
from .models import ColorScheme, HighScore

class ColorSchemeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ColorScheme
        fields = "__all__"


class HighScoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = HighScore
        fields = "__all__"
