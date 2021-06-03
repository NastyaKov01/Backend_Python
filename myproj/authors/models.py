from django.db import models

class Author(models.Model):
    name = models.CharField(verbose_name="Имя автора", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["id"]
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"