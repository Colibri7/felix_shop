# Generated by Django 3.2.4 on 2021-06-29 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brandmodel',
            name='image',
            field=models.ImageField(default=1, upload_to='brands'),
            preserve_default=False,
        ),
    ]
