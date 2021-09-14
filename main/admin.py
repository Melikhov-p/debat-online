from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class ThemeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'rating')
    search_fields = ('name',)

class DebatAdmin(admin.ModelAdmin):
    list_display = ('id', 'theme', 'thesis')
    search_fields = ('thesis', 'theme')


admin.site.register(Theme, ThemeAdmin)
admin.site.register(Debat, DebatAdmin)