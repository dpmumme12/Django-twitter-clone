# Generated by Django 3.1.2 on 2020-10-14 00:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0003_auto_20201013_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='post_liked',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='post', to='network.post'),
        ),
    ]
