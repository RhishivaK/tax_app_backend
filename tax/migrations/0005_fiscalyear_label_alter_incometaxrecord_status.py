# Generated by Django 4.2.8 on 2024-04-13 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tax", "0004_alter_fiscalyear_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="fiscalyear",
            name="label",
            field=models.CharField(default="", max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="incometaxrecord",
            name="status",
            field=models.CharField(
                choices=[
                    ("pending", "Pending"),
                    ("paid", "Paid"),
                    ("dispute", "In dispute"),
                ],
                max_length=10,
            ),
        ),
    ]
