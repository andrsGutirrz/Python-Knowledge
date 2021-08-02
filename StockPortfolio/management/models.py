from django.db import models


# objetos y base

class User(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Investment(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0.0)

    def __str__(self):
            return f'Portfolio: {self.portfolio}, symbol: {self.symbol}, quantity: {self.quantity}, price: {self.price}'

#Historial
class Transaction(models.Model):
    investment = models.ForeignKey(Investment, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    type = models.BooleanField(default=True)
    quantity = models.IntegerField(default=1)
    TransactionPrice = models.FloatField(default=0.0)

    def __str__(self):
            return f'Investment: {self.investment}, date: {self.date}, type: {self.type}, quantity: {self.quantity}, Transacion price: {self.TransactionPrice}'
