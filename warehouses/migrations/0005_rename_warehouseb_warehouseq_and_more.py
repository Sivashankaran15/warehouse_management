# Generated by Django 5.0 on 2024-07-31 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warehouses', '0004_remove_warehouseb_in_time_remove_warehouseb_out_time_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WarehouseB',
            new_name='WarehouseQ',
        ),
        migrations.RenameModel(
            old_name='WarehouseC',
            new_name='WarehouseT',
        ),
        migrations.RenameModel(
            old_name='WarehouseD',
            new_name='WarehouseY',
        ),
    ]
