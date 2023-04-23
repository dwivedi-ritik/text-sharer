from rest_framework import serializers
from textshare.models import Textshare


class TextshareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Textshare
        fields = ['id', 'body', 'created_at', 'updated_at']
