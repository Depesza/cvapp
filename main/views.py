from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic.edit import UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import View
from main.models import Dane, DaneForm
from .forms import UserForm, LoginForm


def index(request):
    return render(request, 'main/home.html')


def cv(request):
    return render(request, 'main/cv.html')


@login_required()
def CvDispDef(request):
    obiekty = Dane.objects.filter(owner=request.user)
    return render(request, 'main/cvdispdef.html', {'obiekty': obiekty})


@login_required()
def OneCvDisp(request, cv_id):
    dane = Dane.objects.get(id=cv_id)
    if str(dane.owner) == str(request.user.username):
        return render(request, 'main/cvtemp.html', {'dane': dane})
    else:
        return HttpResponseRedirect('unacc')


@login_required()
def cvcreate(request):
    if request.method == 'POST':
        form = DaneForm(request.POST, request.FILES)
        form.instance.owner = request.user
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DaneForm()
    return render(request, 'main/cvcreate.html', {
        'form': form
    })


def unacc(request):
    return render(request, 'main/unacc.html')


class CvEdit(UpdateView):
    model = Dane
    fields = ['name', 'lastname', 'email', 'street', 'photo']
    success_url = reverse_lazy('cvdispdef')


class CvDelete(DeleteView):
    model = Dane
    # jeżeli sukces -> przekierowanie
    success_url = reverse_lazy('cvdispdef')


class UserFormView(View):
    form_class = UserForm
    template_name = 'main/registration_form.html'

    # if request.method == "POST" or "GET"
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # unifikacja
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')

        return render(request, self.template_name, {'form': form})


def loginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.add_message(request, messages.INFO, 'Zalogowano.')
                    return redirect('home')
        messages.add_message(request, messages.INFO, 'Błędny login lub hasło.')
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})


def login2(request):
    messages.add_message(request, messages.INFO, 'Aby uzyskać dostęp należy się zalogować.')
    return redirect('login')

def logoutView(request):
    logout(request)
    messages.add_message(request, messages.INFO, 'Zostałeś wylogowany.')
    return redirect('home')
