# Generated by Django 3.0.5 on 2021-08-08 05:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0042_auto_20210808_0029'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brand',
            old_name='names',
            new_name='name',
        ),
    ]
