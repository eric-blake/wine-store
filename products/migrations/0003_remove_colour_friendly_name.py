# Generated by Django 3.2.23 on 2024-01-18 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20240118_1940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='colour',
            name='friendly_name',
        ),
    ]