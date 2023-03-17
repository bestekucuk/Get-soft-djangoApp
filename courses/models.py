from django.db import models
from django.utils.text import slugify

# Create your models here.

class Course(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    imageUrl=models.CharField(max_length=50,blank=True)
    date=models.DateField()
    isActive=models.BooleanField()
    slug=models.SlugField(default="",blank=True,editable=False ,null=False,unique=True, db_index=True)
    def __str__(self):
      return f"{self.title} {self.date}"
    
    def save(self,*args, **kwargs ):
       self.slug=slugify(self.title)
       return super().save(args,kwargs)
class Category(models.Model):
    name=models.CharField(max_length=30)
    slug=models.CharField(max_length=50)
    def __str__(self):
       return f"{self.name}"