# Generated by Django 5.0 on 2024-07-16 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouses', '0002_outtimetracking_remove_commontracking_out_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='commontracking',
            name='out_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='commontracking',
            name='product_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='outtimetracking',
            name='product_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='warehouseb',
            name='product_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='warehousec',
            name='product_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='warehoused',
            name='product_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
