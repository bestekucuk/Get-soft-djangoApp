import os
from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.urls import reverse
from datetime import date,datetime
from django.contrib.auth.decorators import login_required,user_passes_test


from courses.forms import CourseCreateForm, CourseEditForm, UploadForm
from .models import Category, Course, Slider, Upload
from django.core.paginator import Paginator
import random
#http://http://127.0.0.1:8000/  => anasayfa
#http://http://127.0.0.1:8000/home => anasayfa
data={
 "programlama":"programlama kategorisine ait kurslar",
 "web-gelistirme":"web-gelistirme kategorisine ait kurslar",
 "mobil-uygulama":"mobil kategorisine ait kurslar,"

}
db={
#vt benzer bir liste olusturalim
  "courses":[
    #objeler ekleyelim
   {
    "title":"javascript kursu",
    "description":"javascript kur aciklamasi",
    "imageUrl":"1.jpg",
    "slug":"javascript-kursu",
    "date": datetime.now(),
    "isActive":True,
    "isUpdated":True
    } ,
     {
    "title":"python kursu",
    "description":"python kurs aciklamasi",
    "imageUrl":"2.jpg",
    "slug":"python-kursu",
    "date": date(2023,1,3), 
    "isActive":False,
    "isUpdated":True
    } , 
    {
    "title":"web gelistirme kursu",
    "description":"javascript kur aciklamasi",
    "imageUrl":"3.jpg",
    "slug":"web-gelistirme",
    "date": date(2023,2,3), 
    "isActive":True,
    "isUpdated":False
    } 

],

  "categories":[{"id":1, "name":"programlama","slug":"programlama"},
                {"id":2, "name":"web gelistirme","slug":"web-gelistirme"},
                {"id":3, "name":"mobil uygulamalar","slug":"mobil-uygulama"}
                ]
}
def index (request):
   #list comphesion 
   #kurslar=[course for course in db["courses"] if course["isActive"]==True]
   kurslar=Course.objects.filter(isActive=1,isHome=1)
   slider=Slider.objects.filter(is_active=True)


   #db den course tablosuna ait objeleri cektik.yukarıda aynı dizinden models klosörünü import ettik
   kategoriler=Category.objects.all()
   #for kurs in kurslar:
    #   if kurs["isActive"] == True:
    #       k.append(kurs)
   return render(request,'courses/index.html',{
       'categories':kategoriler,
       'courses':kurslar,
       'slider':slider,
       }
       )
#obje olusturduk ve listeyi atadık.wieva gidip for döngüsü ile menüye cevirecegiz.
"""def create_course(request):
  if request.method=="POST":
     title=request.POST["title"]
     description=request.POST["description"]
     image = request.FILES.get("image")
     slug=request.POST["slug"]
     isActive=request.POST.get("isActive",False)
     isHome=request.POST.get("isHome",False)
     if isActive=="on":
        isActive=True  #checkbox secili olanları on olarak gönderir.
     if isHome== "on":
        isHome=True
     kurs=Course(title=title,description=description,image=image,slug=slug,isActive=isActive,isHome=isHome)
     kurs.save()
     return redirect("/kurs")
  return render(request,"courses/create-course.html") #get metoduyla geliyorsa form sayfasını yeniden göndeririz."""
#formda submite basıldıgında gelen bilgileri request.post metodu ile formdan alıp degişkenen atarız sonrasında veritabanına göndeririz.
def isAdmin(user):
   return user.is_superuser
@user_passes_test(isAdmin)
def create_course2(request):
   """if not request.user.is_authenticated:
      return redirect("index")   #kullanıcı girişi yoksa methoda basıldıgında anasayfaya yönlendirir."""
   if request.method=="POST":
      form=CourseCreateForm(request.POST,request.FILES)
      if form.is_valid():
        course = form.save(commit=False)
        course.image = request.FILES["image"]
        course.save()
        return redirect("/kurs")
   else:
     form=CourseCreateForm()  
   return render(request,"courses/create-course2.html",{"form":form})
@login_required() #kulanıcı giriş yaptıysa login ekranına yönlendirir.
def course_list(request):
   kurslar=Course.objects.all()
   return render (request , 'courses/course-list.html',
                  { 'courses':kurslar} )

def course_edit(request, id):
   kurs = get_object_or_404(Course, pk=id)
   if request.method == "POST":
      form = CourseEditForm(request.POST, request.FILES, instance=kurs)
      if form.is_valid():
         course = form.save(commit=False)
         course.save()
         form.save()
         return redirect("course_list")
   else:
      form = CourseEditForm(instance=kurs)
   
   return render(request, 'courses/course-edit.html', {'form': form})

def search(request):
    if "q" in request.GET and request.GET["q"] != "":
      q=request.GET["q"]
      courses = Course.objects.filter( isActive=True,title__contains=q).order_by("date")
      categories = Category.objects.all()
    else:
       return redirect("/kurs") 
    
    paginator = Paginator(courses, 2)
    page = request.GET.get('page', 1)
    page_obj = paginator.page(page)

    return render(request, 'courses/list.html', {
        'categories': categories,
        'page_obj': page_obj,
    })
def course_delete(request,id):
    course=get_object_or_404(Course,pk=id)
    if request.method=="POST":
       course.delete()
       return redirect("course_list")
    return render (request,'courses/course-delete.html',
                   {'course':course})
def upload(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form = Upload(image=request.FILES["image"])
            form.save()
            return render(request, "courses/success.html")
    else:
        form = UploadForm()
    return render(request, "courses/upload.html", {"form": form})
"""
def handle_uploaded_files(file):
   number=random.randint(1,99999)
   filename,file_extention=os.path.splitext(file.name)
   name=filename+"_"+str(number)+file_extention
   with open("temp/"+name,"wb+") as destination:
      for chunk in file.chunks():
         destination.write(chunk)
"""
def kurslar(request):
    list_items=''
    category_list=list(data.keys())
    for category in category_list:
        redirect_url=reverse('courses_by_category',args=[category])
        list_items += f"<li>  <a href='{redirect_url}'>{category}</a></li>"
        html=f"<h1>kurs listesi</h1> <br> <ul>{list_items} </ul>"
    return HttpResponse(html)
def details(request,slug):
   try:
    course= Course.objects.get(slug=slug)
   except:
       raise Http404()
   #kısayol-->>> course=get_object_or_404(Course,pk_kurs_id)
   context= {
       'course':course
   }
   return render(request,'courses/details.html',context)
"""
------------------------------
def getCourseByCategory(request,category_name):
   text=""
   if(category_name=="programlama"):
     text="programlama kategorisine ait kurlar"
   elif(category_name=="web-gelistirme"):
      text="web heliştirme kategorisine ait kurslar"
   else:
       text="yanlış kategori seçimi"
   return HttpResponse(text)
     -------------------------
"""
def getCourseByCategory(request, slug):
    courses = Course.objects.filter(categories__slug=slug, isActive=True).order_by("date")
    categories = Category.objects.all()
    paginator = Paginator(courses, 2)
    page = request.GET.get('page', 1)
    page_obj = paginator.page(page)
    return render(request, 'courses/list.html', {
        'categories': categories,
        'page_obj': page_obj,
        'seciliKategori': slug,
        'tumkurslar':courses,
    })

def getCourseByCategoryId(request,category_id):
    category_list=list(data.keys())
    if(category_id>len(category_list)):
        return HttpResponseNotFound("yanlış kategori seçimi")
    category_name=category_list[category_id-1]
    redirect_url=reverse('courses_by_category',args=[category_name])

    return redirect(redirect_url)




"""
Named Paths-> url deki isimler heryer de tekrar ettiğinde heryerden degiştirmek zorunda kalacağımız için path leri dinamik hale döndürüyoruz
name=degişken_ismi
reverse ('degişken_ismi yani path adı',args=[path in aldıgı parametre degiskeni]) -->>burada ikinci bir parametre varsa bir tane daha args eklenir.
"""
#redirect yönlendirme
#dinamik url
'''paginator
   paginator=Paginator(kurslar,2) kurslar listesini 2 li ayırır.
   page=1  ya da  page=request.Get.get('page',1)  dersek urldeki girilen page degerine(yani request) göre o sayfayı gösterir.1 default degerdir url de girilmez ise otomatik ilk sayfayı gösterir.
   kurslar=paginator.get_page(page)   kurslar listesinin ilk ikisini döndürür sadece
    
   '''
