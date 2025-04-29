from django.db import models

# Create your models here.
class data (models.Model):
    Name = models.CharField(max_length=200)
    photo = models.ImageField(null=True, blank= True)
    video =  models.CharField(max_length=200,  null = True,blank=True)
    funfact = models.CharField(max_length= 10000, null = True,blank=True)
    description = models.CharField(max_length= 10000, null = True,blank=True)

    def __str__(self):
         return self.Name
    
    @property
    def imageURL(self):
         try:
             url = self.photo.url
         except:
             url = ""
         return url