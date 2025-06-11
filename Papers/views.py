from django.db import models
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .serializers import PaperSerializer
from .models import Paper
from account.permissions import IsSuperAdminOrReviewer

# Create your views here.

@swagger_auto_schema(
    method='GET',
    manual_parameters=[
        openapi.Parameter(
            'search',
            openapi.IN_QUERY,
            description="Search by title or author",
            type=openapi.TYPE_STRING
        )
    ],
    responses={200: PaperSerializer(many=True)}
)
@api_view(['GET'])
def paper_list(request):
    search_query = request.GET.get('search', '')

    if search_query:
        papers = Paper.objects.filter(
            models.Q(title__icontains=search_query) |
            models.Q(author__icontains=search_query)
        )
    else:
        papers = Paper.objects.all()

    paginator = PageNumberPagination()
    paginator.page_size = 10
    result_page = paginator.paginate_queryset(papers, request)
    serializer = PaperSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

@swagger_auto_schema(method='post', responses = {200: PaperSerializer(many=True)})
@api_view(['POST'])
@permission_classes([IsSuperAdminOrReviewer])
def paper_create(request):
    paper = Paper.objects.create(**request.data)
    serializer = PaperSerializer(paper)
    return Response(serializer.data)


@swagger_auto_schema(method='patch', request_body=PaperSerializer, responses={200: PaperSerializer()})
@swagger_auto_schema(method='put', request_body=PaperSerializer, responses={200: PaperSerializer()})
@api_view(['PUT', 'PATCH'])
@permission_classes([IsSuperAdminOrReviewer,IsAdminUser,IsSuperAdminOrReviewer])
def paper_update(request, pk):
    paper = Paper.objects.get(pk=pk)

    if request.method == 'PATCH':
        serializer = PaperSerializer(instance=paper, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        serializer = PaperSerializer(instance=paper, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@swagger_auto_schema(method='delete', responses = {200: PaperSerializer(many=True)})
@api_view(['DELETE'])
@permission_classes([IsSuperAdminOrReviewer])
def paper_delete(request, pk):
    paper = Paper.objects.get(pk=pk)
    paper.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

