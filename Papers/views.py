from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from .serializers import PaperSerializer
from .models import Paper


# Create your views here.

@swagger_auto_schema(method='GET', responses = {200: PaperSerializer(many=True)})
@api_view(['GET'])
def paper_list(request):
    paper = Paper.objects.all()
    serializer = PaperSerializer(paper, many=True)
    return Response(serializer.data)

@swagger_auto_schema(method='post', responses = {200: PaperSerializer(many=True)})
@api_view(['POST'])
@permission_classes([IsAdminUser, IsAuthenticated])
def paper_create(request):
    paper = Paper.objects.create(**request.data)
    serializer = PaperSerializer(paper)
    return Response(serializer.data)

@swagger_auto_schema(method='put', request_body=PaperSerializer, responses = {200: PaperSerializer(many=True)})
@api_view(['PUT'])
@permission_classes([IsAdminUser, IsAuthenticated])
def paper_update(request, pk):
    paper = Paper.objects.get(pk=pk)
    serializer = PaperSerializer(paper, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='delete', responses = {200: PaperSerializer(many=True)})
@api_view(['DELETE'])
@permission_classes([IsAdminUser, IsAuthenticated])
def paper_delete(request, pk):
    paper = Paper.objects.get(pk=pk)
    paper.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

