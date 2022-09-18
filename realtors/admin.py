from django.contrib import admin
from .models import Realtor

# Register your models here.

@admin.register(Realtor)
class RealtorAdmin(admin.ModelAdmin):
    '''Admin View for Realtor'''

    list_display = ('name', 'phone', 'email', 'hire_date',)
    list_filter = ('name',)
    search_fields = ('name',)
    list_per_page = 25