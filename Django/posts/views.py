# posts/views.py

from django.views.generic import TemplateView
from django.shortcuts import render


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


def calculatorPageView(request):
    result = ''
    if request.method == 'POST':
        fnum = request.POST.get('fnumber')
        lnum = request.POST.get('lnumber')
        symbol = request.POST.get('symbol')
        if symbol == '+':
            result = int(fnum) + int(lnum)
        if symbol == '-':
            result = int(fnum) - int(lnum)
        if symbol == '/':
            result = int(fnum) // int(lnum)
        if symbol == '*':
            result = int(fnum) * int(lnum)
        print(fnum, lnum, symbol)
    return render(request, 'calculator.html', {'result': result})


# Create your views here.
