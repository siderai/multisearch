from django.db import models


class App(models.Model):
    name = models.TextField()
    paid = models.BooleanField()

    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.TextField()
    paid = models.BooleanField()

    def __str__(self):
        return self.name
