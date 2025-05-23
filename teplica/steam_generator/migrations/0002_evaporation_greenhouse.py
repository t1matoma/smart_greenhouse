# Generated by Django 5.1.5 on 2025-01-30 06:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("steam_generator", "0001_initial"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="evaporation",
            name="greenhouse",
            field=models.OneToOneField(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="users.greenhouse",
            ),
            preserve_default=False,
        ),
    ]
