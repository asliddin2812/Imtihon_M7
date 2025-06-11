from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from .models import Requirements
from .serializers import RequirementsSerializer


@swagger_auto_schema(method='get', responses={200: RequirementsSerializer(many=True)})
@api_view(['GET'])
def requirement_list(request):
    requirement = Requirements.objects.all()
    serializer = RequirementsSerializer(requirement, many=True)
    return Response(serializer.data)

@swagger_auto_schema(method='post', request_body=RequirementsSerializer, response={201: RequirementsSerializer})
@api_view(['post'])
@permission_classes([IsAdminUser, IsAuthenticated])
def requirement_create(request):
    serializers = RequirementsSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='put', request_body=RequirementsSerializer, response={200: RequirementsSerializer})
@api_view(['PUT'])
@permission_classes([IsAdminUser, IsAuthenticated])
def requirement_update(request, pk):
    requirement = Requirements.objects.get(pk=pk)
    serializers = RequirementsSerializer(requirement, data=request.data, partial=True)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_200_OK)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='delete', response={200: RequirementsSerializer})
@api_view(['DELETE'])
@permission_classes([IsAdminUser, IsAuthenticated])
def requirement_delete(request, pk):
    requirement = Requirements.objects.get(pk=pk)
    requirement.delete()
    return Response(status=status.HTTP_200_OK)

