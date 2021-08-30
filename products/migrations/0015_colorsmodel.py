# Generated by Django 3.2.4 on 2021-07-16 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_delete_typemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColorsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=15, null=True)),
                ('code', models.CharField(max_length=12)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'color',
                'verbose_name_plural': 'colors',
            },
        ),
    ]
