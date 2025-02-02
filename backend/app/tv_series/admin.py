from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Viking, Norseman, NFLPlayer

admin.site.register(Viking)
admin.site.register(Norseman)
admin.site.register(NFLPlayer)

# (Optional) Add Django Admin & API for Viewing Scraped Data