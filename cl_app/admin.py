from django.contrib import admin
from cl_app.models import Listing, Profile
# Register your models here.

admin.site.register(Profile)

class ListingAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']

admin.site.register(Listing, admin_class=ListingAdmin)
