# Generated by Django 3.2.4 on 2021-06-30 13:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0003_productsmodel_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsmodel',
            name='wishlist',
            field=models.ManyToManyField(related_name='wishlist', to=settings.AUTH_USER_MODEL),
        ),
    ]