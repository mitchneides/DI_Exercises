# Generated by Django 3.0.4 on 2020-03-24 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20200324_1249'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, help_text='Useful but not required', max_length=100, null=True)),
                ('state', models.CharField(blank=True, help_text='Useful but not required', max_length=100, null=True)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Transportation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transportation_method', models.CharField(choices=[('A', 'Airplane'), ('Bu', 'Bus'), ('Bi', 'Bike'), ('C', 'Car'), ('H', 'Hike'), ('M', 'Motorcycle'), ('S', 'Ship'), ('T', 'Train'), ('W', 'Walk')], default='C', help_text='Select any relevant', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name your trip', max_length=80)),
                ('start_date', models.DateField(blank=True, help_text='Useful but not required', null=True)),
                ('end_date', models.DateField(blank=True, help_text='Useful but not required', null=True)),
                ('destinations', models.ManyToManyField(to='account.Destination')),
                ('transportation_methods', models.ManyToManyField(blank=True, related_name='Travel_methods', to='account.Transportation')),
                ('travelers', models.ManyToManyField(to='account.Profile')),
            ],
        ),
    ]
