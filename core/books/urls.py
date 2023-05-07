from django.urls import path
from .views import BooksList, BooksDetail, BooksCreate, BooksUpdate, BooksDelete

urlpatterns = [
    path('', BooksList.as_view()),
    path('<int:pk>', BooksDetail.as_view(), name='books_detail'),
    path('add/', BooksCreate.as_view(), name='books_create'),
    path('<int:pk>/update/', BooksUpdate.as_view(), name='books_update'),
    path('<int:pk>/delete/', BooksDelete.as_view(), name='books_delete'),
]