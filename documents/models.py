from django.db import models


class App(models.Model):
    name = models.TextField()
    paid = models.BooleanField()


class Game(models.Model):
    name = models.TextField()
    paid = models.BooleanField()
