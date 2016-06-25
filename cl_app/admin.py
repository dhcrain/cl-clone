from django.contrib import admin
from cl_app.models import Listing, Profile, City, ListingType
# Register your models here.

admin.site.register(Profile)


class ListingAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'listing_city', 'category']

admin.site.register(Listing, ListingAdmin)


class CityAdmin(admin.ModelAdmin):
    list_display = ['city']

admin.site.register(City)


class ListingTypeAdmin(admin.ModelAdmin):
    list_display = ['pk', 'parent', 'name']

admin.site.register(ListingType, ListingTypeAdmin)


# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['listing_type', 'category']
#
# admin.site.register(Category, CategoryAdmin)
