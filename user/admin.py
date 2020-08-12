from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from . models import Profile

class ProfileAdmin(ModelAdmin):
    list_display = ["image", "phon"]

admin.site.register(Profile,ProfileAdmin)
