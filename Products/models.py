from django.db import models

# Create your models here.
class CategoryLevel1(models.Model):
    id=models.AutoField(primary_key=True)
    category1=models.CharField(max_length=100)
    category1desc=models.TextField()
    
    def _str_(self):
        return self.category1
    
class CategoryLevel2(models.Model):
    id=models.AutoField(primary_key=True)
    category1=models.ForeignKey(CategoryLevel1,on_delete=models.CASCADE)
    category2=models.CharField(max_length=100)
    category2desc=models.TextField()
    
    def _str_(self):
        return self.category2
    
class CategoryLevel3(models.Model):
    id=models.AutoField(primary_key=True)
    category2=models.ForeignKey(CategoryLevel2,on_delete=models.CASCADE)
    category3=models.CharField(max_length=100)
    category3desc=models.TextField()
    
    def _str_(self):
        return self.category3