from django.urls import path

from .views import (
    requirement_list,
    requirement_create,
    requirement_update,
    requirement_delete
)
urlpatterns = [
    path('', requirement_list, name='requirement_list'),
    path('create/', requirement_create, name='requirement_create'),
    path('update/<pk>/', requirement_update, name='requirement_update'),
    path('delete/<pk>/', requirement_delete, name='requirement_delete'),
]