from django.contrib import admin

# Register your models her
from fpapp.models import CurrentList, FavoriteList

admin.site.register(CurrentList)
admin.site.register(FavoriteList)
