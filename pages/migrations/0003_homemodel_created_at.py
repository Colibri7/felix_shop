# Generated by Django 3.2.4 on 2021-07-01 10:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_homemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='homemodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
