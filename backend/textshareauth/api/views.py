from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse, request as request2

from textshareauth.models import Textshareauth
from textshareauth.api.serializers import TextshareAuthSerializer


from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def textshare_view(request):
    if request.method == 'GET':
        textshares = Textshareauth.objects.filter(created_by=request.user.id)
        serialzed_data = TextshareAuthSerializer(textshares, many=True)
        return Response(serialzed_data.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        request.data["created_by"] = request.data.get(
            "created_by", request.user.id)
        new_textshare = TextshareAuthSerializer(data=request.data)
        if new_textshare.is_valid():
            new_textshare.save()
            return Response(new_textshare.data, status=status.HTTP_201_CREATED)
        return Response(new_textshare.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def textshare_update_delete(request, id):
    try:
        textshare = Textshareauth.objects.get(id=id)
    except Textshareauth.DoesNotExist:
        return Response('Not Found', status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        textshare_serial = TextshareAuthSerializer(textshare)
        return Response(textshare_serial.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        textshare.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        updated_textshare = TextshareAuthSerializer(textshare, request.data)
        updated_textshare.save()
        return Response(updated_textshare.data, status=status.HTTP_202_ACCEPTED)
