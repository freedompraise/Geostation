# Generated by Django 4.0.6 on 2022-08-21 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0002_alter_city_max_alter_city_min_alter_city_temp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=225, unique=True),
        ),
    ]