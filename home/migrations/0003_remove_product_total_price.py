# Generated by Django 5.1.3 on 2024-11-19 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='total_price',
        ),
    ]
