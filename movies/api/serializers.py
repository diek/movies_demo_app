from rest_framework.serializers import ModelSerializer, SerializerMethodField
from ..models import Movie


class MovieSerializer(ModelSerializer):

    cast = SerializerMethodField()

    def get_cast(self, obj):
        return [actor.name for actor in obj.cast.all()]

    class Meta:
        model = Movie
        fields = ['title',
                  'release_date',
                  'cast']