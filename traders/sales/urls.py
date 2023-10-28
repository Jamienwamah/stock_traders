from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('', views.login_request, name="login"),
    path('register/', views.register_request, name="register"),
    path('dashboard/', views.dashboard, name="dashboard"),
    #path('simulate_trader_performance_view', simulate_trader_performance_view, name='simulate_trader_performance_view'),
]
