# Generated by Django 3.0.3 on 2022-10-28 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0006_auto_20221006_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='iva',
            field=models.DecimalField(decimal_places=2, default=10.0, max_digits=9),
        ),
    ]
