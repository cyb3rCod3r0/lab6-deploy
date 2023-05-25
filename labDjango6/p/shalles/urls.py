from . import views
from django.urls import path

urlpatterns = [

    path('shalle1',views.shalle1, name = 'shalle1'),
    path('shalle2', views.shalle2, name = 'shalle2'),
    path('shalle3', views.shalle3, name = 'shalle3'),
    path('shalle4', views.shalle4, name = 'shalle4')
]