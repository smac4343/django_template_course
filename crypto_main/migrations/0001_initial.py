# Generated by Django 4.2 on 2024-04-24 13:29

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Assets",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=20, verbose_name="Название Биржы"),
                ),
                ("types", models.CharField(verbose_name="Тип актива")),
                ("price", models.FloatField(verbose_name="Стоимость актива")),
            ],
            options={
                "verbose_name": "Активы",
            },
        ),
        migrations.CreateModel(
            name="Exchange",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=20, verbose_name="Название Биржы"),
                ),
                (
                    "location",
                    models.CharField(max_length=250, verbose_name="Адрес биржы"),
                ),
                ("trade_volume", models.FloatField(verbose_name="Объем торгов")),
            ],
            options={
                "verbose_name": "Биржа",
                "verbose_name_plural": "Биржи",
            },
        ),
        migrations.CreateModel(
            name="Deals",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.UUID("2ee08552-4d51-4f71-827d-c9ae614554c0"),
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("buying", models.FloatField(verbose_name="Цена покупки")),
                ("selling", models.FloatField(verbose_name="Цена продажи")),
                ("profit", models.TimeField(verbose_name="Прибыль")),
                ("time", models.TimeField(verbose_name="Время сделки")),
                (
                    "asset",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="crypto_main.assets",
                    ),
                ),
                (
                    "buying_ID",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="buying_deals",
                        to="crypto_main.exchange",
                    ),
                ),
                (
                    "selling_ID",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="selling_deals",
                        to="crypto_main.exchange",
                    ),
                ),
            ],
            options={
                "verbose_name": "Сделки",
            },
        ),
    ]
