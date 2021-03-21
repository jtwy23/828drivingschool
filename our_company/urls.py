from django.urls import path
from . import views


urlpatterns = [
    path('about_us.html', views.about_us, name='about_us'),
    path('areas_covered.html', views.areas_covered, name='areas_covered'),
    path('our_cars.html', views.our_cars, name='our_cars'),
]
