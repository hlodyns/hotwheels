# Generated by Django 4.0.6 on 2022-08-23 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_alter_car_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='author',
        ),
    ]