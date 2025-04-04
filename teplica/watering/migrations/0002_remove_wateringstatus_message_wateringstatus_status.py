# Generated by Django 5.1.5 on 2025-01-28 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("watering", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="wateringstatus",
            name="message",
        ),
        migrations.AddField(
            model_name="wateringstatus",
            name="status",
            field=models.CharField(
                choices=[("started", "Начался полив"), ("stopped", "Полив остановлен")],
                default="stopped",
                max_length=10,
            ),
        ),
    ]
