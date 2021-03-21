from django.shortcuts import render

# Create your views here.


def theory(request):

    return render(request, 'learn_to_drive/theory.html')


def practical(request):

    return render(request, 'learn_to_drive/practical.html')


def pass_plus(request):

    return render(request, 'learn_to_drive/pass_plus.html')
