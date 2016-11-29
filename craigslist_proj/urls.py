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
from cl_api.views import ListingListCreateAPIView, ListingRetrieveUpdateAPIView, CategoryListCreateAPIView, CategoryRetriveUpdateAPIView, SubCategoryListCreateAPIView, SubCategoryRetriveUpdateAPIView, CategoryListingListAPIView, SubCategoryListingListAPIView, UserCreateAPIView
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.authtoken import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', IndexView.as_view(), name='index_view'),
    url(r'^register/$', RegisterView.as_view(), name='register_view'),
    url(r'^register/profile/$', ProfileView.as_view(), name='profile_view'),
    url(r'^search/$', SearchListView.as_view(), name='search_list_view'),
    url(r'^listingcreate/(?P<categorypk>\d+)$', ListingCreateView.as_view(), name='listing_create_view'),
    url(r'^listingupdate/(?P<pk>\d+)$', ListingUpdateView.as_view(), name='listing_update_view'),
    url(r'^listingdelete/(?P<pk>\d+)$', ListingDeleteView.as_view(), name='listing_delete_view'),
    url(r'^listing/(?P<pk>\d+)/$', ListingDetailView.as_view(), name='listing_detail_view'),
    url(r'^catergory/(?P<categorypk>\d+)/$', CategoryListView.as_view(), name='category_list_view'),
    url(r'^city/(?P<city>\d+)/$', CityListView.as_view(), name='city_list_view'),
    url(r'^city/(?P<citypk>\d+)/(?P<categorypk>\d+)/$', CityCategoryListView.as_view(), name='city_category_list_view'),
    # Start API urls
    url(r'^api/api-token-auth/', views.obtain_auth_token),
    url(r'^api/register/$', UserCreateAPIView.as_view(), name='create_user_view'),
    url(r'^api/listings/$', ListingListCreateAPIView.as_view(), name='listing-list'),
    url(r'^api/listings/(?P<pk>\d+)/$', ListingRetrieveUpdateAPIView.as_view(), name='listing-detail'),

    url(r'^api/categories/$', CategoryListCreateAPIView.as_view(), name='categories-list'),
    url(r'^api/categories/(?P<pk>\d+)/$', CategoryRetriveUpdateAPIView.as_view(), name='categories-detail'),

    url(r'^api/sub_categories/$', SubCategoryListCreateAPIView.as_view(), name='sub-categories-list'),
    url(r'^api/sub_categories/(?P<pk>\d+)/$', SubCategoryRetriveUpdateAPIView.as_view(), name='sub-categories-detail'),

    url(r'^api/category_listings/(?P<pk>\d+)/$', CategoryListingListAPIView.as_view(), name='category-listings-list'),
    url(r'^api/sub_category_listings/(?P<pk>\d+)/$', SubCategoryListingListAPIView.as_view(), name='sub-category-listings-list'),
    url(r'^api/docs/', include('rest_framework_docs.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
