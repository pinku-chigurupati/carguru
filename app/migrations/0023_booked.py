# Generated by Django 3.2.3 on 2021-05-18 19:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_carbook_carname'),
    ]

    operations = [
        migrations.CreateModel(
            name='booked',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='null', max_length=50)),
                ('status', models.CharField(default='null', max_length=100)),
                ('date', models.DateTimeField(default=datetime.date(2021, 5, 19))),
                ('time', models.DateTimeField(default=datetime.date(2021, 5, 19))),
            ],
        ),
    ]