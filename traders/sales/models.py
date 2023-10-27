from django.db import models

#Create your models

class Trader(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=100.00)
    performance = models.FloatField(default=0.0)  # Set your desired default value here
    total_profit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)



class Tracker(models.Model):
    name = models.CharField(max_length=100)
    performance = models.FloatField()
    total_profit = models.DecimalField(max_digits=10, decimal_places=2)

