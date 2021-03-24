from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Lesson

# Create your views here.


def all_lessons(request):
    """ A view to show all lessons """

    lessons = Lesson.objects.filter(lesson_type='lesson')
    blocks = Lesson.objects.filter(lesson_type='block')
    intensives = Lesson.objects.filter(lesson_type='intensive')
    query = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'lesson_name':
                sortkey = 'lower_name'
                lessons = lessons.annotate(lower_name=Lower('lesson_name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            lessons = lessons.order_by(sortkey)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter some kind of search criteria")
                return redirect(reverse('lessons'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            lessons = lessons.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'lessons': lessons,
        'blocks': blocks,
        'intensives': intensives,
        'search_term': query,
        'current_sorting': current_sorting,
    }

    return render(request, 'lessons/all_lessons.html', context)


def lesson_info(request, lesson_type, pk):
    """ A view to show lesson information """

    lesson = get_object_or_404(Lesson, pk=pk, lesson_type=lesson_type)

    context = {
        'lesson': lesson,
    }

    return render(request, 'lessons/lesson_info.html', context)


def lessons(request, lesson_type):
    """ A view to show lesson information """

    lessons = Lesson.objects.filter(lesson_type=lesson_type)

    context = {
        'lessons': lessons,
    }

    return render(request, 'lessons/lessons.html', context)
