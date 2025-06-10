from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .models import AskedQuestions
from .serializers import AskedQuestionsSerializer


@swagger_auto_schema(method = 'get', responses={200: AskedQuestionsSerializer(many=True)})
@api_view(['get'])
@permission_classes([AllowAny])
def QuestionsList(request):
    questions = AskedQuestions.objects.all()
    serializer = AskedQuestionsSerializer(questions, many=True)
    return Response(serializer.data)

@swagger_auto_schema(method = 'post', request_body= AskedQuestionsSerializer, responses={200: AskedQuestionsSerializer(many=True)})
@api_view(['post'])
@permission_classes([IsAdminUser])
def QuestionsCreate(request):
    serializer = AskedQuestionsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method = 'put', request_body=AskedQuestionsSerializer,responses={200: AskedQuestionsSerializer(many=True)})
@api_view(['PUT'])
@permission_classes([IsAdminUser])
def QuestionsUpdate(request, pk):
    question = AskedQuestions.objects.get(pk=pk)
    serializer = AskedQuestionsSerializer(question, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method = 'delete', responses={200: AskedQuestionsSerializer(many=True)})
@api_view(['delete'])
@permission_classes([IsAdminUser, IsAuthenticated])
def QuestionsDelete(request, pk):
    question = AskedQuestions.objects.get(pk=pk)
    question.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


