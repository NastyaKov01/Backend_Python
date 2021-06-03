from users.models import User
from rest_framework import serializers
from books.serializers import BookSerializer


class UserSerializer(serializers.ModelSerializer):
    book = BookSerializer(many=True)
    class Meta:
        model = User
        #fields = "__all__"
        fields = ['id', 'last_name', 'first_name', 'book']