from django.shortcuts import render
from .models import Lessons, Blocks, Intensive

# Create your views here.


def all_lessons(request):
    """ A view to show all lessons """

    lessons = Lessons.objects.all()
    blocks = Blocks.objects.all()
    intensive = Intensive.objects.all()

    context = {
        'lessons': lessons,
        'blocks': blocks,
        'intensive': intensive,
    }

    return render(request, 'lessons/lessons.html', context)
