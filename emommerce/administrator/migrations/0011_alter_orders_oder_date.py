# Generated by Django 4.2 on 2023-04-23 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0010_cart_item_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='oder_date',
            field=models.DateField(blank=True, default='', null=True),
        ),
    ]
