# Generated by Django 5.0 on 2024-01-16 16:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0003_fotografia_publicada'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='data_publicada',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
