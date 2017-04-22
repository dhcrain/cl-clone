# from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth import get_user_model
from cl_app.models import Listing, ListingType
from cl_api.serializers import ListingSerializer, ListingTypeSerializer, UserSerializer
from cl_api.permissions import IsOwnerOrReadOnly, IsSuperUserOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.


class ListingListCreateAPIView(generics.ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ListingRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ListingTypeSerializer
    permission_classes = (IsSuperUserOrReadOnly,)

    def get_queryset(self):
        return ListingType.objects.filter(parent=None)


class CategoryRetriveUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = ListingTypeSerializer
    permission_classes = (IsSuperUserOrReadOnly,)

    def get_queryset(self):
        return ListingType.objects.filter(parent=None)


class SubCategoryListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ListingTypeSerializer
    permission_classes = (IsSuperUserOrReadOnly,)

    def get_queryset(self):
        return ListingType.objects.exclude(parent=None)


class SubCategoryRetriveUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = ListingTypeSerializer
    permission_classes = (IsSuperUserOrReadOnly,)

    def get_queryset(self):
        return ListingType.objects.exclude(parent=None)


class CategoryListingListAPIView(generics.ListAPIView):
    serializer_class = ListingSerializer

    def get_queryset(self, **kwargs):
        cat_pk = self.kwargs.get('pk')
        return Listing.objects.filter(category__parent=cat_pk)


class SubCategoryListingListAPIView(generics.ListAPIView):
    serializer_class = ListingSerializer

    def get_queryset(self, **kwargs):
        cat_pk = self.kwargs.get('pk')
        return Listing.objects.filter(category=cat_pk)


class UserCreateAPIView(generics.CreateAPIView):
    model = get_user_model()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer
