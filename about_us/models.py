from django.db import models


# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=525)
    duration = models.CharField(max_length=108)
    grade = models.CharField(max_length=255)
    poster_url = models.CharField(max_length=2025)
    book_url = models.CharField(max_length=2025)


class ComingMovie(models.Model):
    name = models.CharField(max_length=525)
    duration = models.CharField(max_length=108)
    grade = models.CharField(max_length=255)
    poster_url = models.CharField(max_length=2025)
    book_url = models.CharField(max_length=2025)