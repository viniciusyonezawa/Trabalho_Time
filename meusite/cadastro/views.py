from django.shortcuts import render

def ola_mundo(request):
    return render(request, 'time.html', {})


def segundapagina(request):
    return render(request, 'segundapagina.html', {})
