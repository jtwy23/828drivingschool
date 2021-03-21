from django.urls import path
from . import views


urlpatterns = [
    path('', views.about_us, name='about_us'),
    path('', views.areas_covered, name='areas_covered'),
    path('', views.our_cars, name='our_cars'),
]
