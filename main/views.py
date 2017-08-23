from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from main.forms import DaneFrom
from main.models import Dane


def index(request):
    return render(request, 'main/home.html')


def cv(request):
    return render(request, 'main/cv.html')


def cvdisp(request):
    cvdane = Dane.objects.all()
    osoba = {
        'dane_cv': list(cvdane)
    }
    return render(request, 'main/cvdisp.html', context=osoba)


def cvadd(request):
    if request.method == 'POST':
        form = DaneFrom(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        c = {'form': form}
        return render(request, 'main/cvadd.html', context=c)
    else:
        form = DaneFrom()
        c = {'form': form}
        return render(request, 'main/cvadd.html', context=c)
