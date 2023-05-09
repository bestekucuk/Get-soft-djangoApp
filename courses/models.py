from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=30)
    slug=models.SlugField(default="",null=False,unique=True,db_index=True,max_length=50)
    def __str__(self):
       return f"{self.name}"
class Course(models.Model):
    title=models.CharField(max_length=50)
    subtitle=models.CharField(max_length=100 ,default="")
    description=RichTextField()
    image=models.ImageField(upload_to="images",default="")
    date=models.DateField(auto_now=True)
    isActive=models.BooleanField(default=False)
    isHome=models.BooleanField(default=False)
    slug=models.SlugField(default="",blank=False ,null=False,unique=True, db_index=True)
   # many to may ilişkisine donusturdugumuz için foreign keye daha fazla ihtiyacımız yok
   #  category= models.ForeignKey(Category,default=1,on_delete=models.CASCADE,related_name="kurslar")
    categories=models.ManyToManyField(Category)
    def __str__(self):
      return f"{self.title} {self.date}"
class Upload(models.Model):
   image=models.ImageField(upload_to="images")
   # upload_to medya dosyasının dizinini belirler media_root dizinine images ekleyip dosyaları yükler.
   
class Slider(models.Model):
    title=models.CharField(max_length=50)
    image=models.ImageField(upload_to="images")
    is_active=models.BooleanField(default=False)
    course=models.ForeignKey(Course,on_delete=models.SET_NULL,null=True,blank=True)
    def __str__(self):
       return f"{self.title}"  #title ı admin sayfasında object olarak gozukurken title a döndürürüz.