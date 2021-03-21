from django.shortcuts import render

# Create your views here.


def about_us(request):

    return render(request, 'our_company/about_us.html')


def areas_covered(request):

    return render(request, 'our_company/areas_covered.html')


def our_cars(request):

    return render(request, 'our_company/our_cars.html')
