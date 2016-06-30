from django.shortcuts import render
from rest_framework import generics
from cl_app.models import Listing
from cl_api.serializers import ListingSerializer
# Create your views here.


class ListingListCreateAPIView(generics.ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class ListingRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
