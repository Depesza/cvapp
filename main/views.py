from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import generic
from main.forms import DaneFrom
from main.models import Dane


def index(request):
    return render(request, 'main/home.html')


def cv(request):
    return render(request, 'main/cv.html')


class CvDisp(generic.ListView):
    template_name = 'main/cvdisp.html'

    def get_queryset(self):
        return Dane.objects.all()
# def cvdisp(request):
#     cvdane = Dane.objects.all()
#     osoba = {
#         'dane_cv': list(cvdane)
#     }
#     return render(request, 'main/cvdisp.html', context=osoba)


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


def danedisp(request, numerid):
    a = get_object_or_404(Dane, pk=numerid)
    return render(request, 'main/cvtemp.html', {'zwrot': a})
    # try:
    #     a = Dane.objects.get(pk=numerid)
    # except Dane.DoesNotExist:
    #     raise Http404("Brak osoby o danym ID.")
    # return render(request, 'main/cvtemp.html', {'zwrot': a})
