# Generated by Django 3.0.5 on 2021-08-04 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0033_auto_20210804_1728'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='proveedor',
            options={'ordering': ['id'], 'verbose_name': 'Proveedor', 'verbose_name_plural': 'Clientes'},
        ),
        migrations.AddField(
            model_name='proveedor',
            name='adress',
            field=models.CharField(default=34, max_length=150, verbose_name='Dirección'),
            preserve_default=False,
        ),
    ]