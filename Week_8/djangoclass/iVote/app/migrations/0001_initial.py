# Generated by Django 3.0.3 on 2020-03-03 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=60)),
                ('votes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tz', models.IntegerField(unique=True)),
                ('name', models.TextField(max_length=60)),
                ('voted', models.BooleanField(default=False)),
            ],
        ),
    ]
