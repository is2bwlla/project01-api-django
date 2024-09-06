from rest_framework import serializers
from .models import Movies

class MoviesSerializer(serializers.ModelSerializer):
    class Meta:                     # o 'meta' é um método do próprio django
        model = Movies
        fields = ['id', 'title', 'genre', 'year', 'language', 'age_rating']
        
        