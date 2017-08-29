from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from main.forms import DaneFrom
from main.models import Dane


def index(request):
    return render(request, 'main/home.html')


def cv(request):
    return render(request, 'main/cv.html')


class CvDisp(generic.ListView):
    template_name = 'main/cvdisp.html'
    # domyślnie:
    # context_object_name = 'object_list'

    def get_queryset(self):
        return Dane.objects.all()


class DaneDisp(generic.DetailView):
    model = Dane
    template_name = 'main/cvtemp.html'


class CvCreate(CreateView):
    model = Dane
    fields = ['name', 'lastname', 'email']


class CvEdit(UpdateView):
    model = Dane
    fields = ['name', 'lastname', 'email']


class CvDelete(DeleteView):
    model = Dane
    # jeżeli sukces -> przekierowanie
    success_url = reverse_lazy('cvdisp')


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
