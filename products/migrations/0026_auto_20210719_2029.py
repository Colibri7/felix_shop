# Generated by Django 3.2.4 on 2021-07-19 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0025_auto_20210719_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttagmodel',
            name='title_en',
            field=models.CharField(max_length=550, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='producttagmodel',
            name='title_ru',
            field=models.CharField(max_length=550, null=True, verbose_name='title'),
        ),
    ]
