from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('search',views.search,name='search'),
    path ('list',views.kurslar),
    path('create-course2',views.create_course2,name='create_course2'),
    path('course-list',views.course_list,name='course_list'),
    path('course-edit/<int:id>',views.course_edit,name='course_edit'),
    path('course-delete/<int:id>',views.course_delete,name='course_delete'),
    path('upload',views.upload,name="upload_image"),
    path ('<slug:slug>',views.details,name="course_details"),
    path('kategori/<int:category_id>',views.getCourseByCategoryId),
    path('kategori/<slug:slug>', views.getCourseByCategory,name='courses_by_category'),
    
 #degisken tanımlayarak dinamik url olusturduk.
]
