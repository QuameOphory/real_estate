from datetime import datetime
from django.utils.translation import gettext_lazy as _
from django.db import models

# Create your models here.

class Realtor(models.Model):
    """Model definition for Realtor."""

    # TODO: Define fields here
    name = models.CharField(_("Name"), max_length=200)
    photo = models.ImageField(_("Photo"), upload_to='photos/%Y/%m/%d/')
    description = models.TextField(_("Description"), blank=True)
    phone = models.CharField(_("Mobile Number"), max_length=50)
    email = models.CharField(_("Email"), max_length=50)
    is_mvp = models.BooleanField(_("Is MVP"), default=False)
    hire_date = models.DateTimeField(_("Hire Date"), blank=True, default=datetime.now)
    class Meta:
        """Meta definition for Realtor."""

        verbose_name = 'Realtor'
        verbose_name_plural = 'Realtors'

    def __str__(self):
        """Unicode representation of Realtor."""
        return self.name

