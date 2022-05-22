from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from django.contrib.auth import login

from django.views.generic import FormView

from webshop_app.forms import UserForm


class HomeView(View):
    def get(self, request):
        return HttpResponse('działa')


class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = UserForm()
        return render(request=request, template_name="base.html", context={
            'form': form
        })

    def post(self, request, *args, **kwargs):
        pass
