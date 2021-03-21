from django.urls import path
from . import views


urlpatterns = [
    path('theory.html', views.theory, name='theory'),
    path('practical.html', views.practical, name='practical'),
    path('pass_plus.html', views.pass_plus, name='pass_plus'),
]
