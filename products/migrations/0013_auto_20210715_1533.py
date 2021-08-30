# Generated by Django 3.2.4 on 2021-07-15 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_gendermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=550)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'type',
                'verbose_name_plural': 'types',
            },
        ),
        migrations.AddField(
            model_name='productsmodel',
            name='gender',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='products', to='products.gendermodel'),
            preserve_default=False,
        ),
    ]
