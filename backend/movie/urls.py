from django.urls import path

from movie import views

# define the urls
urlpatterns = [
    path('movies/', views.movies),
]

