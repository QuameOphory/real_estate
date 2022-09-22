from django.contrib import admin
from .models import Contact
# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    '''Admin View for Contact'''

    list_display = ('listing', 'listing_id', 'name', 'email', 'phone', 'message', 'user_id',)
    list_display_links = ('name',)
    list_per_page = 25
    search_fields = ('name', 'email', 'listing',)
