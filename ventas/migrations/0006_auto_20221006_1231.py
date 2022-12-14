# Generated by Django 3.0.3 on 2022-10-06 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0005_detventa_venta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detventa',
            name='producto_id',
            field=models.ForeignKey(db_column='producto_id', on_delete=django.db.models.deletion.CASCADE, to='ventas.Producto'),
        ),
        migrations.AlterField(
            model_name='detventa',
            name='venta',
            field=models.ForeignKey(db_column='venta_id', on_delete=django.db.models.deletion.CASCADE, to='ventas.Venta'),
        ),
    ]
