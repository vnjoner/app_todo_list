# Generated by Django 3.1.13 on 2021-08-16 04:06

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('task', models.TextField()),
                ('created_time', models.DateField(default=datetime.datetime(2021, 8, 16, 4, 6, 58, 605425))),
                ('finished_time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
