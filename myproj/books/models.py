from django.db import models
from authors.models import Author
from genres.models import Genre

class Book(models.Model):
    title = models.CharField(verbose_name="Название книги", max_length=100)
    author = models.ForeignKey(Author, null=True, blank=True, on_delete=models.SET_NULL,
                               verbose_name="Автор книги")
    year = models.IntegerField(verbose_name="Год первой публикации", default=0)
    price = models.IntegerField(verbose_name="Цена", default=0)
    genre = models.ManyToManyField(Genre, verbose_name="Жанр книги")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["id"]
        verbose_name = "Книга"
        verbose_name_plural = "Книги"