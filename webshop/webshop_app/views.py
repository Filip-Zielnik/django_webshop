from django.contrib import auth, messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from .models import Profile

from .forms import LoginForm, RegistrationForm, UpdateUserForm
from webshop_app.models import Product


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request=request, template_name="home.html")


class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm
        context = {
            'form': form
        }
        return render(request=request, template_name="login.html", context=context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('logged')
            else:
                form.add_error(None, 'Niepoprawny login lub hasło!')
        context = {
            'form': form
        }
        return render(request, 'login.html', context)


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return render(request, 'logout.html')


class RegistrationView(View):
    def get(self, request, *args, **kwargs):
        form = RegistrationForm
        context = {
            'form': form
        }
        return render(request=request, template_name="registration.html", context=context)

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            user = User.objects.create(
                username=username,
                password=password,
                first_name=first_name,
                last_name=last_name,
                email=email,
            )

            user.set_password(password)
            user.save()
        return HttpResponse('dodano użytkownika')


class LoggedView(View):
    def get(self, request, *args, **kwargs):
        return render(request=request, template_name="logged.html")


class CpuView(View):
    def get(self, request, *args, **kwargs):
        form = Product.objects.filter(category_id='1')
        context = {
            'form': form
        }
        return render(request=request, template_name="category.html", context=context)


class GpuView(View):
    def get(self, request, *args, **kwargs):
        form = Product.objects.filter(category_id='2')
        context = {
            'form': form
        }
        return render(request=request, template_name="category.html", context=context)


class MotherboardView(View):
    def get(self, request, *args, **kwargs):
        form = Product.objects.filter(category_id='3')
        context = {
            'form': form
        }
        return render(request=request, template_name="category.html", context=context)


class ProductView(View):
    def get(self, request, product):
        form = Product.objects.filter(product=product)
        context = {
            'form': form
        }
        return render(request=request, template_name="product.html", context=context)


class UpdateUserView(View):
    def get(self, request, *args, **kwargs):
        user_form = UpdateUserForm
        context = {
            'form': user_form
        }
        return render(request=request, template_name="profile.html", context=context)

    def profile(self, request):
        if request.method == 'POST':
            user_form = UpdateUserForm(request.POST, instance=request)

            if user_form.is_valid():
                user_form.save()
                messages.success(request, 'Your profile is updated successfully')
                return redirect(to='users-profile')
        else:
            user_form = UpdateUserForm(instance=request.user)

        return render(request, 'profile.html', {'user_form': user_form})
