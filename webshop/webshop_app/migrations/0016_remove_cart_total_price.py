# Generated by Django 3.2.13 on 2022-06-16 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webshop_app', '0015_order_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='total_price',
        ),
    ]
