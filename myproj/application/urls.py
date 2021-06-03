"""myproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from authors.views import AuthorViewSet
from genres.views import GenreViewSet
from books.views import BookViewSet
from users.views import UserViewSet
from users.views import submit, after_submit

router = DefaultRouter()
router.register(r'authors', AuthorViewSet, basename='authors')
router.register(r'genres', GenreViewSet, basename='genres')
router.register(r'books', BookViewSet, basename='books')
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('books/', include('books.urls')),
    #path('genres/', include('genres.urls')),
    #path('authors/', include('authors.urls')),
    #path('users/', include('users.urls')),
    path('users/submit/', submit, name='submit'),
    path('all_right/', after_submit, name='after_submit')
]

urlpatterns += router.urls