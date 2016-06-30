from cl_app.models import Listing
from rest_framework import serializers

class ListingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Listing
        fields = ['id', 'user', 'listing_city', 'category', 'title', 'price', 'description', 'photo', 'created']
