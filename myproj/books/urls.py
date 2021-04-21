from django.urls import path
from books.views import create
from books.views import get_list
from books.views import get_details
from books.views import index

urlpatterns = [
    path('<str:book_title>/<str:book_author>/<int:pub_year>/<int:book_price>/', create, name='create'),
    path('booklist/', get_list, name='get_list'),
    path('<int:book_id>/', get_details, name='get_details'),
    path('', index, name='index'),
]