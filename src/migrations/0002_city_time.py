# Generated by Django 4.0.6 on 2022-08-15 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
