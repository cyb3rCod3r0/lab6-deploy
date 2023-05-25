from django.urls import path
from . import views

urlpatterns = [

    path('', views.home , name = 'home'),
    path('about',views.about,name= 'about'),
    path('faq',views.faq, name = 'fAQ'),
    path('contact',views.contact, name = 'contact us'),
    #path('shalle', views.shalles, name = 'shalle')

]