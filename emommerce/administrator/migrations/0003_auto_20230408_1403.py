# Generated by Django 3.1 on 2023-04-08 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0002_auto_20230408_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
