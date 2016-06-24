from django.contrib import admin
from cl_app.models import Listing, Profile, City, ListingType, Category
# Register your models here.

admin.site.register(Profile)


# class ListingAdmin(admin.ModelAdmin):
#     list_display = ['title', 'price']

admin.site.register(Listing)


class CityAdmin(admin.ModelAdmin):
    list_display = ['city']

admin.site.register(City, CityAdmin)


class ListingTypeAdmin(admin.ModelAdmin):
    list_display = ['listing_type']

admin.site.register(ListingType, ListingTypeAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['listing_type', 'category']

admin.site.register(Category, CategoryAdmin)
