# Generated by Django 3.0.4 on 2020-03-18 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trading', '0003_team_funds'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='on_trade_block',
            field=models.BooleanField(default=False),
        ),
    ]
