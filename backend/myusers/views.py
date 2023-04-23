from django.shortcuts import render
from django.http import request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from myusers.utils import get_tokens_for_user
from myusers.serializer import MyUserSerializer
# Create your views here.


@api_view(['POST'])
def signup(request):
    new_user = MyUserSerializer(data=request.data)
    if not new_user.is_valid():
        return Response(new_user.errors, status=status.HTTP_400_BAD_REQUEST)
    new_user = new_user.save()
    token = get_tokens_for_user(new_user)
    return Response(token, status=status.HTTP_200_OK)
