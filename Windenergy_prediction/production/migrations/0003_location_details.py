# Generated by Django 3.0.7 on 2020-06-25 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0002_wind_details_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='location_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('lattitude', models.CharField(max_length=100)),
                ('longtitude', models.CharField(max_length=100)),
            ],
        ),
    ]