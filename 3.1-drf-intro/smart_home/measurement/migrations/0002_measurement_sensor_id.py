# Generated by Django 5.0.7 on 2024-07-11 10:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='sensor_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owners', to='measurement.sensor'),
        ),
    ]
