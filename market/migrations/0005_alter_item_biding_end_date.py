# Generated by Django 4.1.7 on 2023-03-16 17:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("market", "0004_alter_item_biding_end_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="biding_end_date",
            field=models.DateTimeField(),
        ),
    ]
