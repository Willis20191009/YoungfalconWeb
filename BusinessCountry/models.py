from django.db import models
from Products.models import CategoryLevel1

# Create your models here.
CONTINENTS=(
    ('1','Asia'),
    ('2','Europe'),
    ('3','South America'),
    ('4','North America'),
    ('5','Africa'),
    ('6','Oceania'),
    ('7','Antarctica'),
    )
    
class CountryList(models.Model):
    id=models.AutoField(primary_key=True)
    cnname=models.CharField(max_length=100)
    enname=models.CharField(max_length=100)
    population=models.CharField(max_length=50)
    area=models.CharField(max_length=50)
    locationarea=models.CharField(max_length=1,choices=CONTINENTS)
    desc_basic=models.TextField()
    desc_weather=models.TextField()
    desc_economy=models.TextField()
    desc_onlinebusiness=models.TextField()
    
    def _str_(self):
        return self.cnname    
    
class CountryFestivals(models.Model):
    country=models.ForeignKey(CountryList,on_delete=models.CASCADE)
    cn_name=models.CharField(max_length=100)
    en_name=models.CharField(max_length=100)
    startdate=models.DateField()
    enddate=models.DateField()
    desc=models.TextField()
    
    def _str_(self):
        return self.cn_name
                        
class Countryfavor(models.Model):
    country=models.ForeignKey(CountryList,on_delete=models.CASCADE)
    category1=models.ManyToManyField(CategoryLevel1)
    specialCategory=models.IntegerField()
    favorProd=models.TextField()
    
    def _str_(self):
        return self.favorProd    