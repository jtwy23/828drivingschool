from django.db import models


class Lessons(models.Model):

    class Meta:
        verbose_name_plural = 'Lessons'

    lesson_image = models.ImageField(null=True, blank=True)
    lesson_image_url = models.URLField(max_length=1024, null=True, blank=True)
    lesson_name = models.CharField(max_length=200)
    lesson_price = models.DecimalField(max_digits=6, decimal_places=2)
    lesson_description = models.TextField()

    def __str__(self):
        return self.lesson_name


class Blocks(models.Model):

    class Meta:
        verbose_name_plural = 'Blocks'

    block_image = models.ImageField(null=True, blank=True)
    block_image_url = models.URLField(max_length=1024, null=True, blank=True)
    block_name = models.CharField(max_length=200)
    block_price = models.DecimalField(max_digits=6, decimal_places=2)
    block_description = models.TextField()

    def __str__(self):
        return self.block_name


class Intensive(models.Model):

    class Meta:
        verbose_name_plural = 'Intensive'

    intensive_image = models.ImageField(null=True, blank=True)
    intensive_image_url = models.URLField(max_length=1024, null=True, blank=True)
    intensive_name = models.CharField(max_length=200)
    intensive_price = models.DecimalField(max_digits=6, decimal_places=2)
    intensive_description = models.TextField()

    def __str__(self):
        return self.intensive_name

