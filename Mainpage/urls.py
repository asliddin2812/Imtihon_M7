from django.urls import path

from .views import Main_pages
urlpatterns = [
    path('', Main_pages, name='main_page'),
]