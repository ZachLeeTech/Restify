# Generated by Django 4.1.6 on 2023-04-03 03:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0004_alter_property_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='rating',
        ),
    ]
