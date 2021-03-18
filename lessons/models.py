from django.db import models

LESSON_TYPE_CHOICES=(
    ("lesson", "Lesson"),
    ("block", "Block"),
    ("intensive", "Intensive"),
)
class Lesson(models.Model):

    class Meta:
        verbose_name_plural = 'Lessons'

    lesson_image = models.ImageField(null=True, blank=True)
    lesson_image_url = models.URLField(max_length=1024, null=True, blank=True)
    lesson_name = models.CharField(max_length=200)
    lesson_price = models.DecimalField(max_digits=6, decimal_places=2)
    lesson_description = models.TextField()
    lesson_type = models.CharField(max_length=200, choices=LESSON_TYPE_CHOICES)

    def __str__(self):
        return self.lesson_name


