# Generated by Django 3.1.3 on 2020-11-22 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20201122_0604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='media/avater.png', upload_to='media/avatar/'),
        ),
    ]
