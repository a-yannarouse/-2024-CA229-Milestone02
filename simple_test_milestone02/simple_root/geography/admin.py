from django.contrib import admin
from .models import Area, Attraction

class AttractionAdmin(admin.TabularInline):
    model = Attraction
    extra = 1

class AreaAdmin(admin.ModelAdmin):
    inlines = [AttractionAdmin]
    
admin.site.register(Area, AreaAdmin)

