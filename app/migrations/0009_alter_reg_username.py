# Generated by Django 3.2 on 2021-05-17 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20210517_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reg',
            name='username',
            field=models.TextField(max_length=20),
        ),
    ]