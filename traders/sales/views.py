from django.shortcuts import render, redirect
from django.http import HttpResponse
from .simulation import simulate_trader_performance 
import plotly.graph_objs as go
from .forms import TraderForm
from .models import Trader


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

def dashboard(request):
    traders = fetch_traders()
    form = handle_form_submission(request)
    graph = generate_plot()
    
    return render(request, 'dashboard.html', {'graph': graph, 'traders': traders, 'form': form})

