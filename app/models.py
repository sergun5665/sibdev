from django.db import models

class Deals(models.Model):
    customer = models.CharField(max_length=100)
    item = models.CharField(max_length=100)
    total = models.FloatField(max_length=12)
    quantity = models.FloatField(max_length=12)
    date = models.DateTimeField()

    def __str__(self):
        return f'{self.customer} {self.item} {self.total}'






# customer - логин    покупателя
#
# item - наименование    товара
#
# total - сумма    сделки
#
# quantity - количество    товара, шт
#
# date - дата   и    время    регистрации    сделки