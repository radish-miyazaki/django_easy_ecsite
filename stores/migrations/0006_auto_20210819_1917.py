# Generated by Django 3.1.6 on 2021-08-19 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0005_orderitems_orders'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='orderitems',
            table='order_items',
        ),
    ]
