# Generated by Django 3.1 on 2023-04-08 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
