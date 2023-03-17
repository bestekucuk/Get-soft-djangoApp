from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path ('list',views.kurslar),
    path ('<slug:slug>',views.details,name="course_details"),
    path('kategori/<int:category_id>',views.getCourseByCategoryId),
    path('kategori/<str:category_name>',views.getCourseByCategory, name='courses_by_category'),
    
 #degisken tanımlayarak dinamik url olusturduk.
]
