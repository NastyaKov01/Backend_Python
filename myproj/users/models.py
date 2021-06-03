from django.db import models
from django.contrib.auth.models import AbstractUser
from books.models import Book

class User(AbstractUser):
    book = models.ManyToManyField(Book, verbose_name="Купленные книги")

    def __str__(self):
       return self.last_name + "_" + self.first_name

    class Meta:
        ordering = ["id"]
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"