# Generated by Django 3.1.2 on 2020-10-15 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0008_delete_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
