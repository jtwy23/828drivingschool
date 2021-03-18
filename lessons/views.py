from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Lessons, Blocks, Intensive

# Create your views here.


def all_lessons(request):
    """ A view to show all lessons """

    lessons = Lessons.objects.all()
    blocks = Blocks.objects.all()
    intensives = Intensive.objects.all()
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

