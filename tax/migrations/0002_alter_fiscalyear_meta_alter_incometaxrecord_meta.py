# Generated by Django 4.2.8 on 2024-04-13 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tax", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fiscalyear",
            name="meta",
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="incometaxrecord",
            name="meta",
            field=models.JSONField(blank=True, null=True),
        ),
    ]
