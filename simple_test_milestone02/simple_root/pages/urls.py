from django.urls import path
from . import views

urlpatterns = [
    path('extra/', views.extra, name = 'extra'),
    path('about/', views.about, name = 'about'),
    path('', views.index, name='index'),
]