# Generated by Django 3.0.3 on 2020-03-03 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='height',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='animal',
            name='legs',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='animal',
            name='speed',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='animal',
            name='weight',
            field=models.IntegerField(default=0),
        ),
    ]
