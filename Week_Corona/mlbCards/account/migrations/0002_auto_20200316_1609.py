# Generated by Django 3.0.4 on 2020-03-16 16:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
                ('rank', models.IntegerField()),
                ('batting_avg', models.IntegerField()),
                ('slg', models.IntegerField()),
                ('homeruns', models.IntegerField()),
                ('rbis', models.IntegerField()),
                ('obp', models.IntegerField()),
                ('runs', models.IntegerField()),
                ('ab', models.IntegerField()),
                ('api_id', models.IntegerField()),
                ('batting_hand', models.CharField(max_length=200)),
                ('team', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='team',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
