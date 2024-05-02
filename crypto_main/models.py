import os
import uuid

from django.db import models

ASSET_TYPES = [
    ("cryptocurrency", "Cryptocurrency"),
    ("fiat", "Fiat"),
]


class Exchange(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=20, verbose_name="Название Биржы")
    location = models.CharField(max_length=250, verbose_name="Адрес биржы")
    trade_volume = models.FloatField(verbose_name="Объем торгов")

    def str(self):
        return self.name

    class Meta:
        verbose_name = "Биржа"
        verbose_name_plural = "Биржи"


class Assets(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=20, verbose_name="Название Биржы")
    types = models.CharField(verbose_name="Тип актива")
    price = models.FloatField(verbose_name="Стоимость актива")

    def str(self):
        return self.name

    class Meta:
        verbose_name = "Активы"


class Deals(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4())
    asset = models.ForeignKey(Assets, on_delete=models.CASCADE)
    buying_ID = models.ForeignKey(
        Exchange, related_name="buying_deals", on_delete=models.CASCADE
    )
    selling_ID = models.ForeignKey(
        Exchange, related_name="selling_deals", on_delete=models.CASCADE
    )
    buying = models.FloatField(verbose_name="Цена покупки")
    selling = models.FloatField(verbose_name="Цена продажи")
    profit = models.TimeField(verbose_name="Прибыль")
    time = models.TimeField(verbose_name="Время сделки")

    def str(self):
        return self.name

    class Meta:
        verbose_name = "Сделки"
