# Generated by Django 5.1.3 on 2024-11-21 13:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='index',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='Photo/')),
                ('Title', models.CharField(max_length=30)),
                ('Price', models.IntegerField()),
                ('Description', models.CharField(max_length=30)),
                ('Rating', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5)])),
            ],
        ),
    ]