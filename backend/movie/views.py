from django.shortcuts import render
# parsing data from the client
from rest_framework.parsers import JSONParser
# To bypass having a CSRF token
from django.views.decorators.csrf import csrf_exempt
# for sending response to the client
from django.http import HttpResponse, JsonResponse
# API definition for task
from .serializers import MovieSerializer, ReviewSerializer
from django.core.paginator import Paginator
# Task model
from .models import Movie, Review
# movie_reviews/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Avg
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer
import time  # For simulation


@csrf_exempt
def movies(request):
    '''
    List all movie
    '''
    if(request.method == 'GET'):
        # get all the movies

        movies = Movie.objects.all()
        paginator = Paginator(movies, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        serializer = MovieSerializer(page_obj, many=True)
        # return a Json response
        return JsonResponse({'data': serializer.data, 'total_pages': paginator.num_pages },safe=False)
    elif(request.method == 'POST'):
        # parse the incoming information
        data = JSONParser().parse(request)
        # instanciate with the serializer
        serializer = MovieSerializer(data=data)
        # check if the sent information is okay
        if(serializer.is_valid()):
            # if okay, save it on the database
            serializer.save()
            # provide a Json Response with the data that was saved
            return JsonResponse(serializer.data, status=201)
            # provide a Json Response with the necessary error information
        return JsonResponse(serializer.errors, status=400)


class MovieDetailView(APIView):
    def get(self, request, movie_id):
        movie = Movie.objects.filter(id=movie_id).prefetch_related('actors').first()
        reviews = Review.objects.filter(film=movie)
        average_grade = reviews.aggregate(Avg('grade'))['grade__avg']

        movie_serializer = MovieSerializer(movie)
        review_serializer = ReviewSerializer(reviews, many=True)


        return Response({
            'movie': movie_serializer.data,
            'reviews': review_serializer.data,
            'average_grade': average_grade
        })

    def put(self, request, movie_id):
        movie = get_object_or_404(Movie, id=movie_id)
        movie_serializer = MovieSerializer(movie, data=request.data)

        if movie_serializer.is_valid():
            movie_serializer.save()
            return Response(movie_serializer.data)
        else:
            return Response(movie_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReviewCreateAPIView(APIView):
    def post(self, request, movie_id):
        try:
            movie = Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            return Response({"error": "Movie not found."}, status=404)

        review_data = request.data.copy()
        review_data["film"] = movie_id
        review_serializer = ReviewSerializer(data=review_data)

        if review_serializer.is_valid():
            review_serializer.save()
            # Simulate the 10-second processing time with Celery (time.sleep)
            time.sleep(10)
            return Response(review_serializer.data, status=201)

        return Response(review_serializer.errors, status=400)