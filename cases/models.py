from django.db import models

# Create your models here.


class covidcasesModel(models.Model):
    city_name=models.CharField(max_length=50)
    cityimageurl=models.URLField(max_length=1000,blank=True,null=True)
    total_cases = models.IntegerField(default=0,blank=True)
    current_cases = models.IntegerField(default=0,blank=True)
    death_cases = models.IntegerField(default=0,blank=True)

    def __str__(self):
        return self.city_name
    