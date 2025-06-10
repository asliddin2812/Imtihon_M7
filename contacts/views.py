from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Contact
from .serializers import ContactSerializer

@swagger_auto_schema(method='get', responses={200: ContactSerializer(many=True)})
@api_view(['GET'])
@permission_classes([IsAdminUser, IsAuthenticatedOrReadOnly])
def contact_list(request):
    queryset = Contact.objects.all()
    serializer = ContactSerializer(queryset, many=True)
    return Response(serializer.data)

@swagger_auto_schema(method='post', request_body=ContactSerializer, response={201: ContactSerializer})
@api_view(['POST'])
@permission_classes([AllowAny])
def contact_post(request):
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='put', request_body=ContactSerializer, response={200: ContactSerializer})
@api_view(['PUT'])
@permission_classes([IsAdminUser, IsAuthenticated])
def contact_put(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    serializer = ContactSerializer(contact, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='delete', responses={204: 'No Content'})
@api_view(['DELETE'])
@permission_classes([IsAdminUser, IsAuthenticated])
def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
