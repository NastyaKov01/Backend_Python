from django.urls import path
from books.views import create, get_list, get_details
from books.views import index, remove, change

urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('list/', get_list, name='get_list'),
    path('<int:id>/', get_details, name='get_details'),
    path('delete/<int:id>', remove, name='remove'),
    path('change/<int:id>', change, name='change')
]