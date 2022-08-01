from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open("data-398-2018-08-30.csv", newline='') as f:
        dict_1 = csv.DictReader(f)
        content = list(dict_1)
        current_page = int(request.GET.get('page', 1))
        paginator = Paginator(content, 10)
        page = paginator.get_page(current_page)
        page_content = page.object_list

        context = {
            'bus_stations': page_content,
            'page': page
    }
    return render(request, 'stations/index.html', context)
