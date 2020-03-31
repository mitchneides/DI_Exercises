# Generated by Django 3.0.4 on 2020-03-30 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_auto_20200329_1058'),
        ('itinerary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dayplan',
            name='contacts',
            field=models.ManyToManyField(blank=True, help_text='Ex: Tour company: 123-456-7890, Tour guide: 098-765-4321, etc.', to='itinerary.Contact'),
        ),
        migrations.AlterField(
            model_name='dayplan',
            name='destinations',
            field=models.ManyToManyField(blank=True, help_text='Ctrl + click to select multiple', to='account.Destination'),
        ),
    ]
