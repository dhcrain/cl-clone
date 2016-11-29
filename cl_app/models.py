from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create your models here.
class City(models.Model):
    city = models.CharField(max_length=20)

    def __str__(self):
        return self.city


class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    profile_city = models.ForeignKey(City, verbose_name='Preferred City', null=True)
    preferred_contact = models.CharField(max_length=30, null=True)

    def __str__(self):
        return str(self.user)


class ListingType(models.Model):
    name = models.CharField(max_length=20)
    parent = models.ForeignKey("self", null=True, blank=True, related_name='subcat')

    def __str__(self):
        return self.name


class Listing(models.Model):
    user = models.ForeignKey('auth.User')
    listing_city = models.ForeignKey(City)
    category = models.ForeignKey(ListingType)
    title = models.CharField(max_length=40)
    price = models.IntegerField()
    description = models.TextField()
    photo = models.ImageField(upload_to="listing_photos", null=True, blank=True, verbose_name="Listing Photo")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']

    @property
    def photo_url(self):
        if self.photo:
            return self.photo.url
        return "/media/listing_photos/classifieds-default.jpg"


@receiver(post_save, sender='auth.User')
def create_user_profile(**kwargs):
    created = kwargs.get("created")
    instance = kwargs.get("instance")
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender='auth.User')
def create_token(**kwargs):
    created = kwargs.get('created')
    instance = kwargs.get('instance')
    if created:
        Token.objects.create(user=instance)
