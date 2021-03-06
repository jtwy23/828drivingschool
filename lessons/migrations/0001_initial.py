# Generated by Django 3.1.7 on 2021-03-10 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lessons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('lesson_image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('lesson_name', models.CharField(max_length=200)),
                ('lesson_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('lesson_description', models.TextField()),
            ],
        ),
    ]
