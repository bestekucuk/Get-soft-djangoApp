from django.contrib import admin
from .models import Course,Category, Slider
# Register your models here.

#ilk yolu
#admin.site.register(Course)
#admin.site.register(Category)
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display= ("title","isActive","slug","category_list","isHome") #listede bu kısımları getirir
    list_display_links=("title","slug",) 
    prepopulated_fields={"slug":("title",),}
   # readonly_fields =("slug",)
    list_filter=("title","isActive","isHome")
    list_editable=("isActive","isHome")
    search_fields=("title","description")

    def category_list(self,obj):
         html=""
         for category in obj.categories.all():
           html += category.name + "  "
         return html
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display= ("name","slug","course_count") #listede bu kısımları getirir
    prepopulated_fields={"slug":("name",),} #name e gore otomik slug verir

    def course_count(self,obj):
        return obj.course_set.count()
        
admin.site.register(Slider)     