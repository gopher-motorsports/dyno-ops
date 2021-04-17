from django.shortcuts import render
import datetime
from .models import Dyno

"""
    Home Page

"""
def home(request):
    context = {}
    return render(request, 'data_entry/home.html', context)


"""
    Data Log Page

    

"""
def collectData(request):
    if request.method == 'POST':
        name = request.POST['name']
        type_ = request.POST['type']
        constant = int(request.POST['constant']) == 0
        throttle = request.POST['throttle']
        rpm = request.POST['rpm']

        Dyno.objects.create(
            name = name,
            test = type_,
            constant = constant,
            throttle = throttle,
            rpm = rpm
        )


        context = {
            'message' : "Data was saved",
        }

        return render(request, 'data_entry/collectdata.html', context)

    else:
        context = {}
        return render(request, 'data_entry/collectdata.html', context)


"""
    View Data Page

"""
def viewData(request):
    if request.method == 'POST':
        # filter data here
        context = {}
        return render(request, 'data_entry/viewdata.html', context)
    # load all entries   
    else:
        entries = Dyno.objects.all()
        context = {'entries': entries}
        return render(request, 'data_entry/viewdata.html', context)
