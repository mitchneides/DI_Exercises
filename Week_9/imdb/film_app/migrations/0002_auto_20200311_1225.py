# Generated by Django 3.0.4 on 2020-03-11 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('film_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('explanation_text', models.CharField(max_length=200)),
                ('image', models.ImageField(null=True, upload_to='')),
            ],
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='director',
            options={'ordering': ['last_name']},
        ),
        migrations.AddField(
            model_name='film',
            name='poster',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='film_app.Poster'),
        ),
    ]
