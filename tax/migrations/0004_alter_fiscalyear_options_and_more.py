# Generated by Django 4.2.8 on 2024-04-13 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tax", "0003_rename_year_fiscalyear_initiate_date_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="fiscalyear",
            options={
                "verbose_name": "Fiscal Year",
                "verbose_name_plural": "Fiscal Years",
            },
        ),
        migrations.AlterModelOptions(
            name="incometaxpolicy",
            options={
                "verbose_name": "Income Tax Policy",
                "verbose_name_plural": "Income Tax Policies",
            },
        ),
        migrations.AlterModelOptions(
            name="incometaxrecord",
            options={
                "verbose_name": "Income Tax Record",
                "verbose_name_plural": "Income Tax Records",
            },
        ),
        migrations.AlterField(
            model_name="fiscalyear",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
