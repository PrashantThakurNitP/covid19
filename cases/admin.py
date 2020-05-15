from django.contrib import admin

# Register your models here.

from .models import covidcasesModel
# Register your models here.
#class covidAdmin(admin.ModelAdmin):
    #readonly_fields=('city_name',)#it says to add readonly field created to admin
admin.site.register(covidcasesModel)
