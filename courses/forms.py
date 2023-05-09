from turtle import textinput
from django import forms
from courses.models import Course


#class CourseCreateForm(forms.Form):
#   title=forms.CharField(label="kurs başlığı",
 #                         required=True,
  #                        error_messages={"required":"kurs başlığı girmelisiniz"},
   #                       widget=forms.TextInput(attrs={"class":"form-control"}))
    #description=forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}))
    #imageUrl=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    #slug=forms.SlugField(widget=forms.TextInput(attrs={"class":"form-control"}))
class CourseCreateForm(forms.ModelForm):
    class Meta:
        model=Course
        #fields=('__all__') dersek hepsini alır
        fields=('title','description','image','slug')
        labels={
            'title':"kurs başlığı",
            'description':"açıklama"
        }
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "description":forms.Textarea(attrs={"class":"form-control"}),
            "image":forms.FileInput(attrs={"class":"form-control"}),
            "slug":forms.TextInput(attrs={"class":"form-control"}),
        }
        error_messages={
            "title":{
             "required":"kurs başlığı girmelisiniz",
             "max_length":"maximum 50 karakter girmelisiniz"
            },
              "description":{
             "required":"kurs açıklaması girmelisiniz",
             "max_length":"maximum 50 karakter girmelisiniz"
            }
        }

class CourseEditForm(forms.ModelForm):
    class Meta:
        model=Course
        #fields=('__all__') dersek hepsini alır
        fields=('title','description','image','slug','categories','isActive')
        labels={
            'title':"kurs başlığı",
            'description':"açıklama",
            'categories':"kategori"
        }
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "description":forms.Textarea(attrs={"class":"form-control"}),
            "image":forms.FileInput(attrs={"class":"form-control"}),
            "slug":forms.TextInput(attrs={"class":"form-control"}),
            "categories":forms.SelectMultiple(attrs={"class":"form-control"}),
            
        }
        error_messages={
            "title":{
             "required":"kurs başlığı girmelisiniz",
             "max_length":"maximum 50 karakter girmelisiniz"
            },
              "description":{
             "required":"kurs açıklaması girmelisiniz",
             "max_length":"maximum 50 karakter girmelisiniz"
            }
        }
class UploadForm(forms.Form):
    image=forms.ImageField(label="İMAGE",
                        required=True,
                         error_messages={"required":"resim uzantılı dosya secniz lütfen"},
                         widget=forms.FileInput(attrs={"class":"form-control"}))