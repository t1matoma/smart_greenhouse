# Generated by Django 5.1.5 on 2025-01-28 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("watering", "0003_wateringstatus_duration_wateringstatus_start_time_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="wateringstatus",
            name="watering_days",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="wateringstatus",
            name="watering_time",
            field=models.TimeField(blank=True, null=True),
        ),
    ]
