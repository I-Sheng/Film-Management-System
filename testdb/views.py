from django.shortcuts import render, redirect
from rest_framework import viewsets
from django.http import HttpResponse

from testdb.serializers import UserSerializer
from testdb.models import Movie
from testdb.forms import MovieForm

class UserViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = UserSerializer

def home(request):
    return HttpResponse("<h1>Welcome to home page</h1>")


def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = Movie(
                title=form.cleaned_data['title'],
                file=request.FILES['file'].read()  # Read the file content into binary
            )
            movie.save()
            return redirect('/upload_success')  # Replace with your success page URL or view
    else:
        form = MovieForm()
    return render(request, 'add_movie.html', {'form': form})

def upload_success(request):
    return HttpResponse("<h1>Upload Success</h1>")
