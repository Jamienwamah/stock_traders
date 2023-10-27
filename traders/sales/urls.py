from django.contrib import admin
from django.urls import path
from . import views
#Create urls here

urlpatterns = [
    path('simulate_trader_performance_view', views.simulate_trader_performance_view, name='simulate_trader_performance_view'),
    path('', views.dashboard, name='dashboard'),
]
