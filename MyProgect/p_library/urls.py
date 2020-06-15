from django.contrib import admin
from django.urls import path, include
from .views import AuthorEdit, AuthorList, author_create_many

urlpatterns = [
    path('author/create', AuthorEdit.as_view(), name='author_create'),
    path('authors', AuthorList.as_view(), name='author_list'),
    path('author/create_many', author_create_many, name='author_create_many'),
]