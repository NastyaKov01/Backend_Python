from books.models import Book
from rest_framework import serializers
from genres.serializers import GenreSerializer
from authors.serializers import AuthorSerializer
from authors.models import Author
from genres.models import Genre
from books.tasks import mail_to_admin

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    genre = GenreSerializer(many=True)

    def create(self, validated_data):
        book = Book.objects.create(
            title = validated_data.get('title'),
            year = validated_data.get('year'),
            price = validated_data.get('price'))
        b_auth = validated_data.get('author').get('name')
        try:
            auth = Author.objects.get(name=b_auth)
        except Author.DoesNotExist:
            auth = Author.objects.create(name=b_auth)
        book.author = auth
        genres = validated_data.get('genre')
        for gnr in genres:
            name = gnr.get('name')
            try:
                genre = Genre.objects.get(name=name)
            except Genre.DoesNotExist:
                genre = Genre.objects.create(name=name)
            book.genre.add(genre)
        book.save()
        mail_to_admin.delay()
        return book

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        b_auth = validated_data.get('author', instance.author).get('name')
        try:
            auth = Author.objects.get(name=b_auth)
        except Author.DoesNotExist:
            auth = Author.objects.create(name=b_auth)
        instance.author = auth
        genres = validated_data.get('genre', instance.genre)
        for gnr in instance.genre.all():
            instance.genre.remove(gnr)
        for gnr in genres:
            name = gnr.get('name')
            try:
                genre = Genre.objects.get(name=name)
            except Genre.DoesNotExist:
                genre = Genre.objects.create(name=name)
            instance.genre.add(genre)
        instance.year = validated_data.get('year', instance.year)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'genre', 'year', 'price',]