from django.urls import path

from .views import (
    QuestionsList,
    QuestionsCreate,
    QuestionsUpdate,
    QuestionsDelete
)

urlpatterns = [
    path('', QuestionsList, name='list'),
    path('create/', QuestionsCreate, name='create'),
    path('update/<int:pk>/', QuestionsUpdate, name='update'),
    path('delete/<int:pk>/', QuestionsDelete, name='delete'),
]