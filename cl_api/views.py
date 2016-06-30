from django.shortcuts import render
from rest_framework import generics
from cl_app.models import Listing, ListingType
from cl_api.serializers import ListingSerializer, ListingTypeSerializer
# Create your views here.


class ListingListCreateAPIView(generics.ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class ListingRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class CategoryListAPIView(generics.ListAPIView):
    serializer_class = ListingTypeSerializer

    def get_queryset(self):
        return ListingType.objects.filter(parent=None)

class CategoryRetriveAPIView(generics.RetrieveAPIView):
    serializer_class = ListingTypeSerializer

    def get_queryset(self):
        return ListingType.objects.filter(parent=None)


class SubCategoryListAPIView(generics.ListAPIView):
    serializer_class = ListingTypeSerializer

    def get_queryset(self):
        return ListingType.objects.exclude(parent=None)


class SubCategoryRetriveAPIView(generics.RetrieveAPIView):
    serializer_class = ListingTypeSerializer

    def get_queryset(self):
        return ListingType.objects.exclude(parent=None)


class CategoryListingListAPIView(generics.ListAPIView):
    serializer_class = ListingSerializer

    def get_queryset(self, **kwargs):
        cat_pk = self.kwargs.get('pk')
        return Listing.objects.filter(category=cat_pk)

class CategoryListingRetriveAPIView(generics.RetrieveAPIView):
    serializer_class = ListingSerializer

    def get_queryset(self, **kwargs):
        cat_pk = self.kwargs.get('pk')
        listing_pk = self.kwargs.get('listing_pk')
        print(cat_pk)
        print(listing_pk)
        return Listing.objects.get(pk=listing_pk)
