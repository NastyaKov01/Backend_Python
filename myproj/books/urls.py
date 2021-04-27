from django.urls import path
from books.views import create
from books.views import get_list
from books.views import get_details
from books.views import index

urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('list/', get_list, name='get_list'),
    path('<int:id>/', get_details, name='get_details'),
]