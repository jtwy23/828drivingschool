from django.shortcuts import render, redirect

# Create your views here.


def view_bag(request):
    """ A view to render the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, lesson_id):
    """ Add a quantity of the specified lessons to the bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if lesson_id in list(bag.keys()):
        bag[lesson_id] += quantity
    else:
        bag[lesson_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)
