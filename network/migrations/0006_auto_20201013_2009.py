# Generated by Django 3.1.2 on 2020-10-14 01:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0005_auto_20201013_1947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='followers',
        ),
        migrations.AddField(
            model_name='profile',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='follower_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='profile',
            name='following',
        ),
        migrations.AddField(
            model_name='profile',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='following_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
