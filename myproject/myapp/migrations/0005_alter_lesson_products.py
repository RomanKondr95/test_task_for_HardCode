# Generated by Django 4.2.5 on 2023-09-24 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_remove_access_last_viewed_lesson_last_viewed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='products',
            field=models.ManyToManyField(to='myapp.product'),
        ),
    ]