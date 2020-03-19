# Generated by Django 3.0.4 on 2020-03-17 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20200316_1719'),
    ]

    operations = [
        migrations.CreateModel(
            name='Roster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Team')),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='roster',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Roster'),
        ),
    ]
