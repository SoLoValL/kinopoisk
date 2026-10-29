from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.contrib.auth import get_user_model
from apps.movies.models import Movie
from apps.ratings.models import Rating, Review


# Create your views here.



class HealthView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        return Response({'status': 'ok'})


class StatsView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        User = get_user_model()
        return Response({
            'movies_count': Movie.objects.filter(is_active=True).count(),
            'users_count': User.objects.count(),
            'ratings_count': Rating.objects.count(),
            'reviews_count': Review.objects.count(),
        })
