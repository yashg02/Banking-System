# Generated by Django 3.1.7 on 2021-08-10 15:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0003_transfer'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]