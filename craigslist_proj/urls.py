"""craigslist_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from cl_app.views import IndexView, RegisterView, SearchListView, ListingUpdateView, ListingDeleteView, ListingTypeCreateView, ListingCreateView, ListingDetailView, ProfileView, CityListView, CategoryListView, CityCategoryListView
from cl_api.views import ListingListCreateAPIView, ListingRetrieveUpdateAPIView, CategoryListAPIView, CategoryRetriveAPIView, SubCategoryListAPIView, SubCategoryRetriveAPIView, CategoryListingListAPIView, CategoryListingRetriveAPIView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', IndexView.as_view(), name='index_view'),
    url('^register/$', RegisterView.as_view(), name='register_view'),
    url('^register/profile/$', ProfileView.as_view(), name='profile_view'),
    url(r'^search/$', SearchListView.as_view(), name='search_list_view'),
    url('^listingcreate/(?P<categorypk>\d+)$', ListingCreateView.as_view(), name='listing_create_view'),
    url('^listingupdate/(?P<pk>\d+)$', ListingUpdateView.as_view(), name='listing_update_view'),
    url('^listingdelete/(?P<pk>\d+)$', ListingDeleteView.as_view(), name='listing_delete_view'),
    url('^listing/(?P<pk>\d+)/$', ListingDetailView.as_view(), name='listing_detail_view'),
    url('^catergory/(?P<categorypk>\d+)/$', CategoryListView.as_view(), name='category_list_view'),
    url('^city/(?P<city>\d+)/$', CityListView.as_view(), name='city_list_view'),
    url('^city/(?P<citypk>\d+)/(?P<categorypk>\d+)/$', CityCategoryListView.as_view(), name='city_category_list_view'),
    url('^api/listings/$', ListingListCreateAPIView.as_view(), name='listing-list'),
    url('^api/listings/(?P<pk>\d+)/$', ListingRetrieveUpdateAPIView.as_view(), name='listing-detail'),
    url('^api/categories/$', CategoryListAPIView.as_view(), name='categories-list'),
    url('^api/categories/(?P<pk>\d+)/$', CategoryRetriveAPIView.as_view(), name='categories-detail'),
    url('^api/sub_categories/$', SubCategoryListAPIView.as_view(), name='sub-categories-list'),
    url('^api/sub_categories/(?P<pk>\d+)/$', SubCategoryRetriveAPIView.as_view(), name='sub-categories-detail'),
    url('^api/category_listings/(?P<pk>\d+)/$', CategoryListingListAPIView.as_view(), name='category-listings-list'),
    url('^api/category_listings/(?P<pk>\d+)/(?P<listing_pk>\d+)/$', CategoryListingRetriveAPIView.as_view(), name='category-listings-detail'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
