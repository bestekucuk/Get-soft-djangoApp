from django.urls import path
from . import views
# . aynı dizini ifade eder.
urlpatterns = [
    path ('',views.home),
    path ('anasayfa',views.home),
    path ('about',views.about),
    path ('contact',views.contact),
]
