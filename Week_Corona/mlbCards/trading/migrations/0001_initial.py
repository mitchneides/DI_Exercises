# Generated by Django 3.0.4 on 2020-03-17 08:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a team name', max_length=200)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Roster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='trading.Team')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
                ('rank', models.IntegerField()),
                ('batting_avg', models.FloatField()),
                ('slg', models.FloatField()),
                ('homeruns', models.IntegerField()),
                ('rbis', models.IntegerField()),
                ('obp', models.FloatField()),
                ('runs', models.IntegerField()),
                ('ab', models.IntegerField()),
                ('api_id', models.IntegerField()),
                ('batting_hand', models.CharField(max_length=200)),
                ('team', models.CharField(max_length=200)),
                ('roster', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='trading.Roster')),
            ],
        ),
    ]
