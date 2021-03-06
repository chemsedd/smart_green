from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from .scripts.requestdata import get_month_records
from tensorflow.keras.models import load_model
from .scripts.prediction_model import make_prediction
from .forms import LandSuitabilityForm
import threading


#
#   dashboard index page
#
@login_required
def index(request):
    # added new feautre
    nbr_pics = range(1, 14)
    return render(request, 'sg_dashboard/index.html', {'title': 'Dashboard', 'nbr_pics': nbr_pics})


#
# Historical data page - with date picker
#
@login_required
def historical_empty(request):
    return render(request, 'sg_dashboard/historical_empty.html', {'title': 'Historical data'})


#
# Get data from the database about the month and the year
#
@login_required
def historical(request, year, month):
    return render(request, 'sg_dashboard/historical.html', context={'title': 'Historical data', 'year': year, 'month': month})


#
# Get data from the database about the month and the year and provide it for API requests
#
@api_view(['GET'])
def historical_api(reques, year, month):
    month_ = month.capitalize()
    results = get_month_records(year, month_)
    return Response(results)


PATH = 'D:\works\master-2\smart_green\sg_dashboard\scripts\lstm_model'
model = None


#
#   Method to handle land suitability prediction form
#
def handleForm(request):
    global model
    # Handling the land suitability form
    form = LandSuitabilityForm(request.POST)
    # check form validity
    if form.is_valid():
        # Precipitation  Relative  Humidity  Pressure  Temp_avg
        precipitation = form.cleaned_data['precipitation']
        humidity = form.cleaned_data['humidity']
        pressure = form.cleaned_data['pressure']
        temperature = form.cleaned_data['temperature']

        prediction = make_prediction(model,
                                     [precipitation, humidity, pressure, temperature])
        report = {
            'result': prediction
        }
        return render(request, 'sg_dashboard/land_suitability.html', {'report': report, 'form': form})


#
#   Get data about land suitability
#
@login_required
def land_suitability(request):
    global model
    # loading the LSTM model
    if model == None:
        model = load_model(PATH)
    # handle form
    if request.method == 'POST':
        return handleForm(request)
    else:
        # Create and render form
        form = LandSuitabilityForm()
        return render(request, 'sg_dashboard/land_suitability.html', {'form': form})
