# Generated by Django 4.2.1 on 2023-05-29 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_remove_cart_price_remove_order_price_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name_plural': 'Cart'},
        ),
    ]
