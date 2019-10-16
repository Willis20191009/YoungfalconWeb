from django.contrib import admin

# Register your models here.
from .models import CountryList,CountryFestivals,Countryfavor

admin.site.register(CountryList)
admin.site.register(CountryFestivals)
admin.site.register(Countryfavor)