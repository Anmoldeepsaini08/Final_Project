# Generated by Django 4.2 on 2023-04-30 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0022_orders_alter_cart_item_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.CharField(max_length=20)),
                ('user_item', models.CharField(max_length=20)),
            ],
        ),
    ]
