# Generated by Django 3.0.4 on 2020-03-24 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20200324_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
