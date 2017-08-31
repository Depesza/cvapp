from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from main.models import Dane
from .forms import UserForm, LoginForm


def index(request):
    return render(request, 'main/home.html')


def cv(request):
    return render(request, 'main/cv.html')


def myCv(request):
    return render(request, 'main/mycv.html')


# class CvDisp(generic.ListView):
#     template_name = 'main/cvdisp.html'
#     # domyślnie:
#     # context_object_name = 'object_list'
#
#     def get_queryset(self):
#         return Dane.objects.all()
#
#
# class CvCreate(CreateView):
#     model = Dane
#     fields = ['name', 'lastname', 'email', 'street']
#
#
# class CvEdit(UpdateView):
#     model = Dane
#     fields = ['name', 'lastname', 'email']
#
#
# class CvDelete(DeleteView):
#     model = Dane
#     # jeżeli sukces -> przekierowanie
#     success_url = reverse_lazy('cvdisp')


def editView(request):

    return render(request, 'main/edit.html')





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
                    return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})


def logoutView(request):
    logout(request)
    return redirect('home')
