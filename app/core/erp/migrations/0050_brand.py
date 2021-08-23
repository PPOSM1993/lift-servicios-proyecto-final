# Generated by Django 3.0.5 on 2021-08-08 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0049_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Marca',
                'verbose_name_plural': 'Marcas',
                'ordering': ['id'],
            },
        ),
    ]