from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse

from testdb.serializers import UserSerializer
from testdb.models import Movie
from testdb.forms import MovieForm

class UserViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = UserSerializer

def home(request):
    return HttpResponse("Welcome to home page")

def form_view(request):
    form = MovieForm()
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, "movie.html", context)
