# Generated by Django 3.2.23 on 2024-03-02 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_alter_product_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(editable=False, max_length=32, null=True, unique=True),
        ),
    ]