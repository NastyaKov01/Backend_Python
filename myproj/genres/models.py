from django.db import models

class Genre(models.Model):
    name = models.CharField(verbose_name="Название жанра", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["id"]
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"