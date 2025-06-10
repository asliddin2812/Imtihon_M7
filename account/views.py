from django.contrib.auth.forms import PasswordResetForm
from drf_yasg import openapi
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView

from .serializers import RegisterSerializer, LoginSerializer

# Register
@swagger_auto_schema(method='post', request_body=RegisterSerializer)
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=201)
    return Response(serializer.errors, status=400)

@swagger_auto_schema(method='post', request_body=LoginSerializer)
@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=200)
        else:
            return Response({'detail': 'Invalid credentials'}, status=401)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    request.user.auth_token.delete()
    return Response({'detail': 'Logged out successfully'}, status=200)

class PasswordResetAPIView(APIView):
    @swagger_auto_schema(
        operation_description="Send password reset email",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='User email')
            }
        ),
        responses={200: 'Password reset email sent', 400: 'Invalid email'}
    )
    def post(self, request):
        email = request.data.get('email')
        if email:
            form = PasswordResetForm({'email': email})
            if form.is_valid():
                form.save(
                    request=request,
                    email_template_name='registration/password_reset_email.html',
                    subject_template_name='registration/password_reset_subject.txt',
                )
                return Response({'message': 'Password reset email sent'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid email'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)