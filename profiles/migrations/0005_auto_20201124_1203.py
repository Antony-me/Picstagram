# Generated by Django 3.1.3 on 2020-11-24 09:03

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_relationship'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=cloudinary.models.CloudinaryField(default='ouao15vmh1c1wecxm5ir', max_length=255, verbose_name='image'),
        ),
    ]
