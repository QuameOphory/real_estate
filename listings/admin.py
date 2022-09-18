from django.contrib import admin
from .models import Listing
# Register your models here.

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    '''Admin View for Listing'''

    list_display = ('realtor','address','city','description','price','bedrooms','bathrooms','garage','sqft','lot_size')
    list_filter = ('title','realtor',)
    search_fields = ('title','price','city',)
