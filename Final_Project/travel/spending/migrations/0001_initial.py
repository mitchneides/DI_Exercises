# Generated by Django 3.0.4 on 2020-03-25 16:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0012_auto_20200325_1025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('buyer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='made_purchase', to='account.Profile')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='spending.Category')),
                ('sharers', models.ManyToManyField(related_name='splitting_purchase', to='account.Profile')),
            ],
        ),
    ]
