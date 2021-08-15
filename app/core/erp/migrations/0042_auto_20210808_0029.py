# Generated by Django 3.0.5 on 2021-08-08 04:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0041_auto_20210805_1037'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=150, verbose_name='Empresa')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(default=41, on_delete=django.db.models.deletion.PROTECT, to='erp.Brand', verbose_name='Marca'),
            preserve_default=False,
        ),
    ]
