# Generated by Django 4.2 on 2023-04-23 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0013_remove_orders_oder_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='oder_date',
            field=models.DateField(blank=True, default='', null=True),
        ),
    ]