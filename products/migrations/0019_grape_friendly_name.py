# Generated by Django 3.2.23 on 2024-03-19 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_rename_reviews_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='grape',
            name='friendly_name',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
