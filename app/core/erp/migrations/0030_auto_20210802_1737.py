# Generated by Django 3.1.7 on 2021-08-02 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0029_auto_20210802_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detsale',
            name='prod',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.product'),
        ),
    ]
