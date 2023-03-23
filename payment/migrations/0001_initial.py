# Generated by Django 4.1.7 on 2023-03-22 18:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("market", "0009_remove_item_payment_information_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Payment",
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
                ("expire_time", models.DateTimeField()),
                ("price", models.IntegerField()),
                ("reminder", models.DateTimeField()),
                ("paid", models.BooleanField(default=False)),
                ("payment_date", models.DateTimeField(blank=True, null=True)),
                (
                    "creditor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="demand_payments",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "debtor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="owed_payments",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "item",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="market.item"
                    ),
                ),
            ],
        ),
    ]
