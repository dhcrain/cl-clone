from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    city = models.CharField(max_length=15)
    contact = models.CharField(max_length=30)


class City(models.Model):
    city = models.CharField(max_length=20)


class ListingType(models.Model):
    listing_type = models.CharField(max_length=20)
    category = models.ForeignKey(self, related_name=None, related_query_name=None, limit_choices_to=None, parent_link=False, to_field=None, db_constraint=True)

    def __str__(self):
        return self.listing_type

class Category(models.Model):
    listing_type = models.ForeignKey(ListingType)
    category = models.CharField(max_length=20)



class Listing(models.Model):
    user = models.ForeignKey('auth.User')
    city = models.ForeignKey(City)
    category = models.ForeignKey(Category, limit_choices_to={'listing_type': 1})
    title = models.CharField(max_length=40)
    price = models.IntegerField()
    description = models.TextField()
    photo = models.ImageField(upload_to="listing_photos", null=True, blank=True, verbose_name="Listing Photo")
    created = models.DateTimeField(auto_now_add=True)

    # @property
    # def photo_url(self):
    #     if self.photo:
    #         return self.photo.url
    #     return "default_photo"


# @receiver(post_save, sender='auth.User')
# def create_user_profile(**kwargs):
#     created = kwargs.get("created")
#     instance = kwargs.get("instance")
#     if created:
#         Profile.objects.create(user=instance)
