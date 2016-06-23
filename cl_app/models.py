from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

CITY_CHOICE = (('gvl', 'Greenville'), ('avl', 'Asheville'), ('clt', 'Charlotte'), ('hou', 'Houston'))

class City(models.Model):
    city = models.CharField(max_length=20)

class Type(models.Model):
    city = models.ForeignKey(City)
    type = models.CharField(max_length=20)

class Category(models.Model):
    city = models.ForeignKey(City)
    type = models.ForeignKey(Type)
    category = models.CharField(max_length=20)

class Profile(models.Model):
    user = models.ForeignKey('auth.User')
    city = models.CharField(max_length=15, choices=CITY_CHOICE)
    contact = models.CharField(max_length=30)


class Listing(models.Model):
    LISTING_CHOICE = (('fs', 'For Sale'), ('re', 'Real Estate'), ('btr', 'Barter'), ('srv', 'Service'))
    CATEGORY_CHOICE = (('owner', 'By-Owner'), ('dealer', 'By-Dealer'))
    user = models.ForeignKey('auth.User')
    city = models.ForeignKey(City)
    listing_type = models.ForeignKey(Type)
    category = models.ForeignKey(Category)
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
