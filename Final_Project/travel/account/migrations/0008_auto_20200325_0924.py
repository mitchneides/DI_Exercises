# Generated by Django 3.0.4 on 2020-03-25 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_trip_completed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trip',
            old_name='completed',
            new_name='status',
        ),
    ]
