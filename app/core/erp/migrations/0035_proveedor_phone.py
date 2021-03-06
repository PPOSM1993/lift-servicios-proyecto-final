# Generated by Django 3.0.5 on 2021-08-04 22:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0034_auto_20210804_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='phone',
            field=models.CharField(blank=True, max_length=17, unique=True, validators=[django.core.validators.RegexValidator(message="El número de telefono debe tener el siguiente: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Telefono'),
        ),
    ]
