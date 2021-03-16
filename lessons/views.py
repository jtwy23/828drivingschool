from django.shortcuts import render
from .models import Lessons

# Create your views here.


def all_lessons(request):
    """ A view to show all lessons """

    lessons = Lessons.objects.all()

    context = {
        'lessons': lessons,
    }

    return render(request, 'lessons/lessons.html', context)
