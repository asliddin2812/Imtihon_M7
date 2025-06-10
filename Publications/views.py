from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from .models import Publications
from .serializers import PublicationsSerializer

# Create your views here.

@swagger_auto_schema(method='get', responses={200: PublicationsSerializer(many=True)})
@api_view(['GET'])
def publications_list(request):
    publications = Publications.objects.all()
    serializer = PublicationsSerializer(publications, many=True)
    return Response(serializer.data)

@swagger_auto_schema(method='post',request_body=PublicationsSerializer, responses={200: PublicationsSerializer(many=True)})
@api_view(['POST'])
@permission_classes([IsAuthenticated,IsAdminUser])
def publications_create(request):
    publications = Publications.objects.all()
    serializer = PublicationsSerializer(publications, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='put', request_body=PublicationsSerializer, responses={200: PublicationsSerializer(many=True)})
@swagger_auto_schema(method='patch', request_body=PublicationsSerializer, responses={200: PublicationsSerializer(many=True)})
@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated,IsAdminUser])
def publications_update(request, pk):
    publications = Publications.objects.get(pk=pk)
    if request.method == 'PATCH':
        serializer = PublicationsSerializer(instance=publications, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        serializer = PublicationsSerializer(instance=publications, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@swagger_auto_schema(method='delete', responses={200: PublicationsSerializer(many=True)})
@api_view(['DELETE'])
@permission_classes([IsAuthenticated,IsAdminUser])
def publications_delete(request, pk):
    publications = Publications.objects.get(pk=pk)
    publications.delete()
    return Response(status=status.HTTP_200_OK)
