# Generated by Django 5.1 on 2024-08-15 16:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("invApp", "0007_alter_product_delivered_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="delivered_date",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 8, 16, 0, 13, 31, 273894)
            ),
        ),
    ]
