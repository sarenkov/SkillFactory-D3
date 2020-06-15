from django.contrib import admin
from django.urls import path, include
from p_library import views
from p_library.views import AuthorEdit, AuthorList, author_create_many, books_authors_create_many, friends_list


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.books_list),
    path('index/', views.index),
    path('index/book_increment/', views.book_increment),
    path('index/book_decrement/', views.book_decrement),
    path('publishers/', views.publishers),
    path('author/create', AuthorEdit.as_view(), name='author_create'),
    path('authors', AuthorList.as_view(), name='author_list'),
    path('author/create_many', author_create_many, name='author_create_many'),
    path('author_book/create_many', books_authors_create_many, name='author_book_create_many'),
    path('friends_list', views.friends_list)
    # path("p_library/", include(("p_library.urls", 'p_library'), namespace="p_library"))
]
