from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request, 'ninjas/index.html')

def ninjas(request):
    colors = {
        'purple',
        'blue',
        'red',
        'orange'
    }
    return render(request, 'ninjas/ninjas.html', {'colors': colors})

def color(request, color):
    if color == 'purple':
        color = {'purple'}
    elif color == 'blue':
        colors = {'blue'}
    elif color == 'red':
        colors = {'red'}
    elif color == 'orange':
        colors = {'orange'}
    else:
        colors = {'april'}
    return render(request, 'ninjas/ninjas.html', {'colors': colors})
