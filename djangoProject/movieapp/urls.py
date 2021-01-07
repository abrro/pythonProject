from django.urls import path
from. import views


app_name = 'movieapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('movies/', views.movies, name='movies'),
    path('movie/<int:id>', views.movie, name='movie'),
    path('movie/edit/<int:id>', views.edit, name='edit'),
    path('movie/new', views.newmovie, name='new'),
    path('signup/', views.register, name='register')
]
