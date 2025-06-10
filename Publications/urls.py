from django.urls import path

from .views import (
    publications_list,
    publications_create,
    publications_update,
    publications_delete
)
urlpatterns = [
    path('', publications_list, name='publications_list'),
    path('create/', publications_create, name='publications_create'),
    path('update/<int:pk>/', publications_update, name='publications_update'),
    path('delete/<int:pk>/', publications_delete, name='publications_delete'),
]