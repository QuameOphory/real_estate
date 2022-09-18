from django.contrib import admin
from .models import Realtor

# Register your models here.

@admin.register(Realtor)
class RealtorAdmin(admin.ModelAdmin):
    '''Admin View for Realtor'''

    list_display = ('name', 'phone', 'email', 'hire_date', 'is_mvp',)
    list_filter = ('name',)
    list_editable = ('is_mvp',)
    search_fields = ('name',)
    list_per_page = 25