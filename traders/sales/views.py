from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from .forms import TraderForm, TrackerForm, UserForm #CustomUserCreationForm
from .models import Trader, Tracker, CustomUser, MyUserModel
import plotly.graph_objs as go
from django.contrib.auth import login, authenticate  # add this
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from django.contrib import messages
from django.db import IntegrityError, transaction
from django.http import HttpResponse







def simulate_trader_performance_view(request):
    simulate_trader_performance()
    return HttpResponse("Simulation complete")

def fetch_traders():
    return Trader.objects.all()

def handle_form_submission(request):
    if request.method == 'POST':
        form = TraderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TraderForm()
    return form

def generate_plot():
    timestamps = ["2023-10-26 09:00:00", "2023-10-26 09:01:00", "2023-10-26 09:02:00"]
    profits = [100, 120, 80]

    trace = go.Scatter(x=timestamps, y=profits, mode='lines')
    data = [trace]

    layout = go.Layout(
        title='Profit vs. Time',
        xaxis=dict(title='Timestamp'),
        yaxis=dict(title='Profit/Loss')
    )
    fig = go.Figure(data=data, layout=layout)

    graph = fig.to_html(full_html=False, default_height=500, default_width=700)
    return graph

@login_required
def dashboard(request):
    traders = fetch_traders()
    form = TraderForm(request.POST) if request.method == 'POST' else TraderForm()
    graph = generate_plot()

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('dashboard')

    return render(request, 'dashboard.html', {'graph': graph, 'traders': traders, 'form': form})

@api_view(['GET'])
def signup(request):
    signup = User.objects.all()
    # many=True means if we want to serialize multiple object or a single object
    serializer = UserSerializer(signup, many=True)
    return Response(serializer.data)


def post(self, request, *args, **kwargs):
    cover = request.data['cover']
    username = request.data['username']
    MyUserModel.objects.create(username=username, cover=cover)
    return HttpResponse({'message': 'Image successfully uploaded'}, status=200)


def register_request(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()  # This will use your custom save method
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("dashboard")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = UserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})



def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("dashboard")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
            # Debugging output
    #print("Form Errors:", form.errors)
    #print("User:", user)
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})

#Try and catch exception errors

def my_view(request):
    try:
        with transaction.atomic():
            # Create a new user (example)
            user = User.objects.create_user(username='newuser', password='password', email='email')
            # Add other code that might raise IntegrityError
    except IntegrityError as e:
        error_message = "A user with this username already exists. Please choose a different username."
        transaction.set_rollback(True)  # Roll back the transaction
        return HttpResponse(error_message, status=400)
    
    
def register_user(request):
    try:
        user = User.objects.create(username='newuser')
    except IntegrityError as e:
        error_message = "A user with this username already exists. Please choose a different username."
        return HttpResponse(error_message, status=400)
    return HttpResponse("User registered successfully.")