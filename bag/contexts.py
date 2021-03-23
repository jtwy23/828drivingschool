from decimal import Decimal
from django.conf import settings


def bag_contents(request):

    bag_items = []
    total = 0
    lesson_count = 0

    if total < settings.FREE_LESSON_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_LESSON_PERCENTAGE / 100)
        free_lesson_delta = settings.FREE_LESSON_THRESHOLD - total
    else:
        delivery = 0
        free_lesson_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'lesson_count': lesson_count,
        'delivery': delivery,
        'free_lesson_delta': free_lesson_delta,
        'free_lesson_threshold': settings.FREE_LESSON_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
