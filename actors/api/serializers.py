from rest_framework.serializers import ModelSerializer, SerializerMethodField
from ..models import Actor


class ActorSerializer(ModelSerializer):

    movies = SerializerMethodField()

    def get_movies(self, obj):
        return [m.title for m in obj.get_movies()]

    class Meta:
        model = Actor
        fields = ['name',
                  'movies']