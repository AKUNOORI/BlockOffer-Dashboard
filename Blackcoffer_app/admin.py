from django.contrib import admin
from .models import EnergyForecast, JsonFile

# Register your models here.

class YourModelAdmin(admin.ModelAdmin):
    list_display = ["end_year", "intensity", "sector", "topic", "insight", "url", "region", "start_year", "impact", "added", "published", "country", "relevance", "pestle", "source", "title", "likelihood"]

admin.site.register(EnergyForecast, YourModelAdmin)
admin.site.register(JsonFile)
