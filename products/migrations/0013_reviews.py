# Generated by Django 3.2.23 on 2024-02-29 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('products', '0012_favourites'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.userprofile')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]