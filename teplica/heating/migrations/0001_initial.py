# Generated by Django 5.1.5 on 2025-01-29 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="HeatingStatus",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("on", "Включено"), ("off", "Выключено")],
                        default="off",
                        max_length=3,
                    ),
                ),
                ("temperature", models.IntegerField(default=20)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
