# Generated by Django 3.0.4 on 2020-04-04 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0016_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='name',
            field=models.CharField(help_text='Name/type of document', max_length=80),
        ),
    ]
