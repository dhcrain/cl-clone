from cl_app.models import Listing, ListingType
from rest_framework import serializers
# from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


class ListingSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Listing
        fields = ['id', 'user', 'listing_city', 'category', 'title', 'price', 'description', 'photo', 'created']


class ListingTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ListingType
        fields = ['id', 'name', 'parent']


# http://www.django-rest-framework.org/api-guide/serializers/#additional-keyword-arguments
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user
