from django.db import models


# Create your models here.
class ECommercePlatforms(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    found_country=models.IntegerField
    found_company=models.CharField(max_length=255)
    found_time=models.DateField()
    desc=models.TextField()
    
    def _str_(self):
        return self.name
    

class Weblinks(models.Model):
    eCommercePlatforms=models.ForeignKey(ECommercePlatforms,on_delete=models.CASCADE)
    linkname=models.CharField(max_length=255)
    countryID=models.IntegerField()
    
    def _str_(self):
        return self.linkname
    
