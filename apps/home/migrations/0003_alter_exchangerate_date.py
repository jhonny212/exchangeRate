# Generated by Django 4.0.4 on 2022-04-15 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_exchange_exchangerate_purchase_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchangerate',
            name='date',
            field=models.DateField(unique=True, verbose_name='Fecha'),
        ),
    ]
