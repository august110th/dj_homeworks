from django.http import HttpResponse
from django.shortcuts import render, reverse
from os import listdir
from datetime import datetime



def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)

def time_view(request):
    current_time = datetime.now().strftime("%H:%M")
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)

def workdir_view(request):
    x = ", ".join(listdir())
    msg = f"Содержимое рабочей директории: {x}"
    return HttpResponse(msg)
