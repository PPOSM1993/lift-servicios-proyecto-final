# Generated by Django 3.0.5 on 2021-08-08 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0051_auto_20210808_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='desc',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Descripción'),
        ),
    ]
