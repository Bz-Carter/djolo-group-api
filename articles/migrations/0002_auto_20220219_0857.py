# Generated by Django 3.2.4 on 2022-02-19 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='price',
            field=models.DecimalField(decimal_places=3, max_digits=12),
        ),
        migrations.AlterField(
            model_name='space',
            name='price',
            field=models.DecimalField(decimal_places=3, max_digits=12),
        ),
    ]
