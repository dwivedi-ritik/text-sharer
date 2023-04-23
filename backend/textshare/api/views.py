from django.shortcuts import render
from django.http import JsonResponse, request
from textshare.models import Textshare
from textshare.api.serializers import TextshareSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


@api_view(['GET', 'POST'])
def textshare_view(request):
    if request.method == 'GET':
        textshares = Textshare.objects.all()
        serialzed_data = TextshareSerializer(textshares, many=True)
        return Response(serialzed_data.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        new_textshare = TextshareSerializer(data=request.data)
        if new_textshare.is_valid():
            new_textshare.save()
            return Response(new_textshare.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def textshare_update_delete(request, id):
    try:
        textshare = Textshare.objects.get(id=id)
    except Textshare.DoesNotExist:
        return Response('Not Found', status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        textshare_serial = TextshareSerializer(textshare)
        return Response(textshare_serial.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        textshare.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        updated_textshare = TextshareSerializer(textshare, request.data)
        updated_textshare.save()
        return Response(updated_textshare.data, status=status.HTTP_202_ACCEPTED)
