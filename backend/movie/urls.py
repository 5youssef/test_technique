from django.urls import path

from movie import views

# define the urls
urlpatterns = [
    path('movies/', views.movies),
    path('movies/<int:movie_id>/', views.MovieDetailView.as_view(), name='movie_detail'),
    path('movies/<int:movie_id>/reviews/', views.ReviewCreateAPIView.as_view(), name='review-create'),

]

