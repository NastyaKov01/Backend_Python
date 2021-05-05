from django.urls import path
from users.views import create, get_list, get_details

urlpatterns = [
    path('', get_list, name='get_list'),
    path('<int:id>/', get_details, name='get_details'),
    path('create/', create, name='create')
]