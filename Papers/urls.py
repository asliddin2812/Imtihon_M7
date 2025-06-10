from django.urls import path

from .views import (
    paper_list,
    paper_create,
    paper_update,
    paper_delete
)
urlpatterns = [
    path('', paper_list, name='paper_list'),
    path('create/', paper_create, name='paper_create'),
    path('update/<int:pk>/', paper_update, name='paper_update'),
    path('delete/<int:pk>/', paper_delete, name='paper_delete'),
]