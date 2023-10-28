from djongo import models
from djongo.models import CharField
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils import timezone
from bson import ObjectId


# Custom User Model compatible with MongoDB
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    # Add other custom fields as needed

    def __str__(self):
        return self.username

# Models using pymongo-compatible fields
class Trader(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=100.00)
    performance = models.FloatField(default=0.0)
    total_profit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name

class Tracker(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    performance = models.FloatField()
    total_profits = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

# Other models using Djongo-specific fields
class MyUserModel(models.Model):
    _id = CharField(primary_key=True, max_length=24, default=1, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    last_login = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.username
