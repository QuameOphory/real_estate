from django.contrib import admin
from .models import Listing
# Register your models here.

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    '''Admin View for Listing'''

    list_display = ('realtor', 'title','is_published','city','state','price','bedrooms','bathrooms','garage','sqft','lot_size')
    list_display_links = ('title',)
    list_editable = ('is_published',)
    list_filter = ('title','realtor',)
    search_fields = ('title','price','city', 'description', 'address', 'state', 'zipcode',)
    list_per_page = 25
