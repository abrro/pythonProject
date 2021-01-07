from django.forms import ModelForm, Form
import django.forms as f
from .models import Movie, Review


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'director', 'year', 'synopsis']


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['summary', 'body']
