# Generated by Django 3.1.13 on 2021-08-16 04:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_auto_20210816_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_time',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
