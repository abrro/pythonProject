from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Movie, Review
from .forms import MovieForm, ReviewForm



def index(req):
    if not req.user.is_authenticated:
        return render(req, 'index.html', {'page_title': 'MovieReview'})
    else:
        return redirect('movieapp:movies')


@login_required
def movies(req):
    temp = Movie.objects.all()
    return render(req, 'movies.html', {'movies': temp})


@login_required
def movie(req, id):
    temp = get_object_or_404(Movie, id=id)

    return render(req, 'movie.html', {'movie': temp, 'page_title': temp.title})


@permission_required('movieapp.change_movie')
def edit(req, id):
    if req.method == 'POST':
        forma = MovieForm(req.POST)

        if forma.is_valid():
            m = Movie.objects.get(pk=id)
            m.title = forma.cleaned_data['title']
            m.director = forma.cleaned_data['director']
            m.year = forma.cleaned_data['year']
            m.synopsis = forma.cleaned_data['synopsis']
            m.save()
            return redirect('movieapp:movies')
        else:
            return render(req, 'edit.html', {'form': forma, 'id': id})
    else:
        temp = get_object_or_404(Movie, id=id)
        forma = MovieForm(instance=temp)
        return render(req, 'edit.html', {'form': forma, 'id': id})


@permission_required('movieapp.add_movie')
def newmovie(req):
    if req.method == 'POST':
        forma = MovieForm(req.POST)

        if forma.is_valid():
            m = Movie(title=forma.cleaned_data['title'],
                      year=forma.cleaned_data['year'],
                      director=forma.cleaned_data['director'],
                      synopsis=forma.cleaned_data['synopsis'],
                      owner=req.user)
            m.save()
            return redirect('movieapp:movies')
        else:
            return render(req, 'new.html', {'form': forma})
    else:
        forma = MovieForm()
        return render(req, 'new.html', {'form': forma})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('movieapp:movies')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
