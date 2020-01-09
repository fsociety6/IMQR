from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from .models import Item
from .forms import LoginForm, RegisterForm


def login_view(request):
    if request.method == "POST":
        loginform = LoginForm(data=request.POST)
        if loginform.is_valid():
            cd = loginform.cleaned_data
            user = authenticate(username=cd['email'], password=cd['password'])
            if user is not None:
                login(request, user)

            else:
                return HttpResponse("UnSuccessFully Login !!!")
    else:
        loginform = LoginForm()
    if request.method == "GET":
        return render(request, "inventory/registration/login.html", {"loginform": loginform})


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'inventory/registration/register.html', {"form": form})


class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    fields = ['name', 'serial_number', 'category', 'details']
    success_url = '/items/create_item'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
