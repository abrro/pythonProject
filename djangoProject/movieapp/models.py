from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime


class Movie(models.Model):
    title = models.CharField(max_length=128)
    director = models.CharField(max_length=64)
    year = models.IntegerField(default=datetime.date.today().year,
                               validators=[MinValueValidator(1888),
                                           MaxValueValidator(datetime.date.today().year)])
    synopsis = models.CharField(max_length=512)
    mark = models.IntegerField()
    num_reviews = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Review(models.Model):
    summary = models.CharField(max_length=64)
    body = models.TextField()
    rating = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(10)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.summary
