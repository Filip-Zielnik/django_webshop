# Generated by Django 3.2.13 on 2022-06-04 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webshop_app', '0009_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='webshop_app/static/media/products'),
        ),
    ]