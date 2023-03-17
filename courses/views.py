from django.shortcuts import redirect, render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from datetime import date,datetime
from .models import Category, Course
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
   kurslar=Course.objects.filter(isActive=1)
   #db den course tablosuna ait objeleri cektik.yukarıda aynı dizinden models klosörünü import ettik
   kategoriler=Category.objects.all()
   #for kurs in kurslar:
    #   if kurs["isActive"] == True:
    #       k.append(kurs)
   return render(request,'courses/index.html',{
       'categories':kategoriler,
       'courses':kurslar}
       )
#obje olusturduk ve listeyi atadık.wieva gidip for döngüsü ile menüye cevirecegiz.
    
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
def getCourseByCategory(request,category_name):
    try:
        category_text =data[category_name];
      #  return HttpResponse(category_text)
        return render(request,'courses/partials/kurslar.html',{
        'category':category_name, 
        'category_text':category_text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
      })
    except:
        return HttpResponseNotFound("yanlış kategori seçimi")

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