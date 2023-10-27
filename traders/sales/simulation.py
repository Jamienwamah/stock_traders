import random
from .models import Trader

def simulate_trader_performance():
    traders = Trader.objects.all()
    
    for trader in traders:
        # Simulate a random profit or loss
        profit_or_loss = random.uniform(-10, 10)  # Random number between -10 and 10
        trader.balance += profit_or_loss
        trader.save()
