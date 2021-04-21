from django.db import models

class Book(models.Model):
    #id = models.IntegerField("Id", default=0)
    title = models.CharField("Title", max_length=100)
    author = models.CharField("Author", max_length=100)
    year = models.IntegerField("Year", default=0)
    price = models.IntegerField("Price", default=0)

    def __str__(self):
        return self.title