# Generated by Django 4.1.7 on 2023-04-05 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0006_merge_20230405_2129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='rating',
        ),
        migrations.AddField(
            model_name='property',
            name='description',
            field=models.CharField(default='description', max_length=500),
            preserve_default=False,
        ),
    ]
