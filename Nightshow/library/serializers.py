from rest_framework import serializers
class movie_posters_serializers(serializers.Serializer):
    title=serializers.ImageField()
    movie=serializers.CharField