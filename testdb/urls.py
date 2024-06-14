"""
URL configuration for yugabyteTest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('add_movie/', views.add_movie),
    path('upload_success', views.upload_success),
    path('movies/', views.movies, name="movies"),
    path('movie_item/<int:pk>/', views.display_movie, name="movie_item"),
    path('video/<int:movie_id>/', views.video_stream, name='video_stream'),
]

