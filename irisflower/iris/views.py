from django.shortcuts import render
from django.http import HttpResponse
from .forms import IrisForm
from .predictor import iris_predictor

def index(request):
    #return HttpResponse('HELLO')

    prediction = ''

    if request.method == 'POST':
    
        form = IrisForm(request.POST)

        if form.is_valid():

            sl = form.cleaned_data['sep_length']
            sw = form.cleaned_data['sep_width']
            pl = form.cleaned_data['pet_length']
            pw = form.cleaned_data['pet_width']

            prediction = iris_predictor(sl , sw , pl , pw)


    form = IrisForm()
    return render(request , 'iris/index.html' , {'form' : form , 'predict' : prediction})
