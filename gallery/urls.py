from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='gallery-home'),
    path('addwheel/', views.addwheel, name='add-new-wheel'),
    path('about/', views.about, name='about'),  
]