# Generated by Django 3.2.23 on 2024-01-18 12:37

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('grape', models.CharField(max_length=32)),
                ('closure', models.CharField(max_length=32)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('typeof', models.CharField(max_length=32)),
                ('region', models.CharField(max_length=32)),
                ('style', models.CharField(max_length=254)),
                ('vintage', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('in_stock', models.BooleanField()),
                ('stock_qty', models.IntegerField()),
            ],
        ),
    ]
