# Generated by Django 3.1.2 on 2020-10-24 19:21

import blog.utilites
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201024_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='text_file',
            field=models.FileField(upload_to=blog.utilites.get_timestamp_path, verbose_name='Рассказ'),
        ),
        migrations.AlterField(
            model_name='story',
            name='title_story',
            field=models.TextField(max_length=50, unique=True, verbose_name='Название'),
        ),
    ]
