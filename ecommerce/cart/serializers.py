from rest_framework import serializers
from .models import Login

class LoginSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Login
        fields = ('id', 'url', 'username', 'phone', 'password')
        