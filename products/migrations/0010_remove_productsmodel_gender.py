# Generated by Django 3.2.4 on 2021-07-13 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_productsmodel_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productsmodel',
            name='gender',
        ),
    ]
