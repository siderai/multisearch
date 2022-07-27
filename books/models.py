from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.TextField()

    def __str__(self):
        return self.title


class Document(models.Model):
    name = models.TextField(default="Nothing")
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.name
