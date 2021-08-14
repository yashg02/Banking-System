# Generated by Django 3.1.7 on 2021-08-10 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0002_auto_20210808_2243'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=20)),
                ('acc1', models.IntegerField()),
                ('bal', models.IntegerField()),
                ('rname', models.CharField(max_length=20)),
                ('acc2', models.IntegerField()),
                ('comment', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
    ]