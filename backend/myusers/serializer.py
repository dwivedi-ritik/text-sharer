from rest_framework import serializers
from myusers.models import MyUser
from django.contrib.auth.hashers import make_password


class MyUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = MyUser
        fields = ['username', 'email',
                  'first_name', 'last_name', 'password']

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        new_user = MyUser.objects.create(**validated_data)
        return new_user

    def get_token(self, user):
        token = super().get_token(user)
        # Add custom claims
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['email'] = user.email
        token['username'] = user.username

        return token
