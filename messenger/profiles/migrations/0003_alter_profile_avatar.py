# Generated by Django 5.0.6 on 2024-07-04 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='avatars/no_avatar.png', null=True, upload_to='avatars/'),
        ),
    ]
