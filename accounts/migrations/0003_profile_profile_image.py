# Generated by Django 5.1.3 on 2024-11-26 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profile_address_alter_profile_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='1.jpg', upload_to='Profile'),
        ),
    ]
