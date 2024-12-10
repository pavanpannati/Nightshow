from rest_framework import serializers
from .models import movie_posters
class movie_posters_serializers(serializers.Serializer):
    class Meta:
        model=movie_posters
        fields=['id','movie','posters','title','image']    