# Generated by Django 3.0.5 on 2021-08-05 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0039_proveedor'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='proveedor',
            field=models.ForeignKey(default=35, on_delete=django.db.models.deletion.PROTECT, to='erp.Proveedor', verbose_name='Proveedor'),
            preserve_default=False,
        ),
    ]
