from rest_framework import serializers, status
from testdb.models import Movie
from django.core.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'file')

