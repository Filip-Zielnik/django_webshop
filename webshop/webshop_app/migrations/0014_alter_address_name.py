# Generated by Django 3.2.13 on 2022-06-07 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webshop_app', '0013_address_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
