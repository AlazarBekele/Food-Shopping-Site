# Generated by Django 5.1.3 on 2024-11-22 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0003_x_icon_dynamic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='index',
            name='Description',
            field=models.TextField(),
        ),
    ]
