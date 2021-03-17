from django.shortcuts import render, get_object_or_404
from .models import Lessons, Blocks, Intensive

# Create your views here.


def all_lessons(request):
    """ A view to show all lessons """

    lessons = Lessons.objects.all()
    blocks = Blocks.objects.all()
    intensives = Intensive.objects.all()

    context = {
        'lessons': lessons,
        'blocks': blocks,
        'intensives': intensives,
    }

    return render(request, 'lessons/lessons.html', context)


def lesson_info(request, pk):
    """ A view to show lesson information """

    lesson = get_object_or_404(Lessons, pk=pk)

    context = {
        'lesson': lesson,
    }

    return render(request, 'lessons/lesson_info.html', context)


def block_info(request, pk):
    """ A view to show block information """

    block = get_object_or_404(Blocks, pk=pk)

    context = {
        'block_lesson': block,
    }

    return render(request, 'blocks/block_info.html', context)


def intensive_info(request, pk):
    """ A view to show intensive information """

    intensive = get_object_or_404(Intensive, pk=pk)

    context = {
        'intensive': intensive,
    }

    return render(request, 'intensive/intensive_info.html', context)

