# Generated by Django 4.2.8 on 2024-04-23 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_user_reward_points_alter_user_middle_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="annual_income",
            field=models.DecimalField(
                blank=True, decimal_places=2, default=0, max_digits=30, null=True
            ),
        ),
    ]
