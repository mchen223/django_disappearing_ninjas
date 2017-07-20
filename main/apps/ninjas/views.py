from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request, 'ninjas/index.html')

def ninjas(request):
    colors = {
        'purple.jpg',
        'blue.jpg',
        'red.jpg',
        'orange.jpg'
    }
    return render(request, 'ninjas/ninjas.html', {'colors': colors})

def color(request, color):
    if color == 'purple':
        colors = {'purple.jpg'}
    elif color == 'blue':
        colors = {'blue.jpg'}
    elif color == 'red':
        colors = {'red.jpg'}
    elif color == 'orange':
        colors = {'orange.jpg'}
    else:
        colors = {'april.jpg'}
    return render(request, 'ninjas/ninjas.html', {'colors': colors})
