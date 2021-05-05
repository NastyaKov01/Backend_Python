from django.db import models
from django.contrib.auth.models import AbstractUser
from books.models import Book

class User(AbstractUser):
    lastname = models.CharField(verbose_name="Фамилия пользователя", max_length=100, default="-")
    firstname = models.CharField(verbose_name="Имя пользователя", max_length=100, default="-")
    book = models.ManyToManyField(Book, verbose_name="Купленные книги")

    def __str__(self):
        return self.lastname + "_" + self.firstname

    class Meta:
        ordering = ["id"]
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"