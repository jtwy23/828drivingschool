from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_lessons, name='all_lessons'),
    path('<str:lesson_type>', views.lessons, name='lessons'),
    path('<str:lesson_type>/<int:pk>', views.lesson_info, name='lesson_info'),
]
