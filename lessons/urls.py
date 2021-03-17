from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_lessons, name='lessons'),
    path('<int:pk>', views.lesson_info, name='lesson_info'),
    path('block/<int:pk>', views.block_info, name='block_info'),
    path('intensive/<int:pk>', views.intensive_info, name='intensive_info'),
]
