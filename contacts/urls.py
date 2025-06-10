from django.urls import path

from .views import (
    contact_list,
    contact_post,
    contact_put,
    contact_delete
)

urlpatterns = [
    path('', contact_list, name='contact-list'),
    path('create/', contact_post, name='contact-create'),
    path('update/<int:pk>/', contact_put, name='contact-update'),
    path('delete/<int:pk>/', contact_delete, name='contact-delete'),
]