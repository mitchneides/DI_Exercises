# Generated by Django 3.0.4 on 2020-03-24 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='funds',
        ),
    ]