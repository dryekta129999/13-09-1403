# Generated by Django 5.1.3 on 2024-11-19 14:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.PositiveSmallIntegerField()),
                ('unit_price', models.PositiveIntegerField()),
                ('discount', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('total_price', models.PositiveIntegerField()),
                ('information', models.TextField(blank=True, null=True)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('available', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to='Product')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category')),
            ],
        ),
    ]
