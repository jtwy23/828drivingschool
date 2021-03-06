# Generated by Django 3.1.7 on 2021-03-10 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blocks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('block_image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('block_name', models.CharField(max_length=200)),
                ('block_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('block_description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Blocks',
            },
        ),
        migrations.CreateModel(
            name='Intensive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intensive_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('intensive_image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('intensive_name', models.CharField(max_length=200)),
                ('intensive_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('intensive_description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Intensive',
            },
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AlterModelOptions(
            name='lessons',
            options={'verbose_name_plural': 'Lessons'},
        ),
    ]
