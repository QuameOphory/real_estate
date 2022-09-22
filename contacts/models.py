from datetime import datetime
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

# Create your models here.

class Contact(models.Model):
    listing = models.CharField(_("Listings"), max_length=250)
    listing_id = models.IntegerField(_("Listing ID"))
    name = models.CharField(_("Name"), max_length=250)
    email = models.CharField(_("Email"), max_length=100)
    phone = models.CharField(_("Phone"), max_length=100)
    message = models.TextField(_("Message"), blank=True)
    contact_date = models.DateTimeField(_("Contact Date & Time"), default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)
    

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")

    def __str__(self):
        return self.name


