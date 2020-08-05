from django.contrib import admin

# Register your models here.
from .models import Asset, Tag

admin.site.register(Asset)
admin.site.register(Tag)
