from datetime import datetime
from django.db import models
from django.utils.translation import gettext_lazy as _
from realtors.models import Realtor

# Create your models here.

class Listing(models.Model):
    """Model definition for Listing."""
    realtor = models.ForeignKey(Realtor, verbose_name=_("Realtor"), on_delete=models.DO_NOTHING)
    title = models.CharField(_("Title"), max_length=50)
    address = models.CharField(_("Address"), max_length=50)
    city = models.CharField(_("City"), max_length=50)
    state = models.CharField(_("State"), max_length=50)
    zipcode = models.CharField(_("ZipCode"), max_length=50)
    description = models.TextField(_("Description"))
    price = models.IntegerField(_("Price"))
    bedrooms = models.IntegerField(_("Bedroom"))
    bathrooms = models.DecimalField(_("Bathroom"), max_digits=2, decimal_places=1)
    garage = models.IntegerField(_("Garage"), default=0)
    sqft = models.IntegerField(_("Sqft"))
    lot_size = models.FloatField(_("Lot Size"))
    is_published = models.BooleanField(_("Is Published"), default=True)
    list_date = models.DateField(_("List Date"), auto_now=False, auto_now_add=False)
    photo_main = models.ImageField(_("Main Photo"), upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(_("Photo 1"), upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(_("Photo 2"), upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(_("Photo 3"), upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(_("Photo 4"), upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(_("Photo 5"), upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(_("Photo 6"), upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(_("Is Published"), default=True)
    list_date = models.DateField(_("List Date"), default=datetime.now)


    # TODO: Define fields here

    class Meta:
        """Meta definition for Listing."""

        verbose_name = 'Listing'
        verbose_name_plural = 'Listings'

    def __str__(self):
        """Unicode representation of Listing."""
        return self.title

