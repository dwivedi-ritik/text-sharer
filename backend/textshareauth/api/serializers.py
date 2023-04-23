from rest_framework import serializers
from textshareauth.models import Textshareauth


class TextshareAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Textshareauth
        fields = ['id', 'title', 'body',
                  'created_by', 'created_at', 'updated_at']
