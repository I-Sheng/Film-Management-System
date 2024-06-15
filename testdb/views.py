from django.shortcuts import render, redirect
from rest_framework import viewsets
from django.http import HttpResponse

from testdb.models import Movie
from testdb.forms import MovieForm

def home(request):
    return render(request, "index.html")


def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = Movie(
                title=form.cleaned_data['title'],
                file=request.FILES['file'].read(),  # Read the file content into binary
                description=form.cleaned_data['description']
            )
            movie.save()
            return redirect('/upload_success')  # Replace with your success page URL or view
    else:
        form = MovieForm()
    return render(request, 'add_movie.html', {'form': form})

def upload_success(request):
    return render(request, "upload_success.html")

def movies(request):
    model_data = Movie.objects.all()
    movies_data = {"movies": model_data}
    return render(request, "movies.html", movies_data)


def display_movie(request, pk=None):
    if pk == None:
        menu_item = ''
    else:
        menu_item = Movie.objects.get(pk=pk)
    return render(request, "movie_item.html", {"movie_item": menu_item})

def video_stream(request, movie_id):
    movie_item = Movie.objects.get(id=movie_id)
    response = HttpResponse(movie_item.file, content_type='video/mp4')
    response['Content-Disposition'] = 'inline; filename="some_filename.mp4"'
    return response