# Generated by Django 3.0.5 on 2021-08-05 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0040_product_proveedor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proveedor',
            old_name='names',
            new_name='name',
        ),
    ]
