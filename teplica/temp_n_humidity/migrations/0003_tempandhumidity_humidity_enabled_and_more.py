# Generated by Django 5.1.5 on 2025-01-29 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("temp_n_humidity", "0002_alter_tempandhumidity_humidity"),
    ]

    operations = [
        migrations.AddField(
            model_name="tempandhumidity",
            name="humidity_enabled",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="tempandhumidity",
            name="temperature_enabled",
            field=models.BooleanField(default=True),
        ),
    ]
