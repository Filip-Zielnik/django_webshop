from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import redirect, render
from django.views import View

from .forms import LoginForm, UserForm, UpdateUserForm, ProfileForm
from .models import Product, Profile


class HomeView(View):
    """ Displays homepage """

    def get(self, request):
        return render(request=request, template_name="home.html")


class RegistrationView(View):
    """ Displays registration form with extended django-user's fields """

    def get(self, request, *args, **kwargs):
        user_form = UserForm
        profile_form = ProfileForm
        context = {
            'user_form': user_form,
            'profile_form': profile_form,
        }
        return render(request=request, template_name="registration.html", context=context)

    def post(self, request, *args, **kwargs):
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            birth_date = profile_form.cleaned_data['birth_date']
            user = user_form.save()
            profile = Profile.objects.create(user=user, birth_date=birth_date)
            profile.save()
            user.set_password(user.password)
            user.save()
        else:
            context = {
                'user_form': user_form,
                'profile_form': profile_form,
            }
            return render(request=request, template_name="registration.html", context=context)
        return render(request=request, template_name="registration_message.html")


class LoginView(View):
    """ Allows user to log in using username & password """

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
        return render(request=request, template_name='login.html', context=context)


class LogoutView(View):
    """ Allows user to log out """

    def get(self, request, *args, **kwargs):
        logout(request)
        return render(request=request, template_name='logout.html')


class LoggedView(LoginRequiredMixin, View):
    """ View ONLY available for logged users """

    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        return render(request=request, template_name="logged.html")


class CpuView(View):
    """ Displays only products in CPU category(id=1) """

    def get(self, request):
        form = Product.objects.filter(category_id='1')
        context = {
            'form': form
        }
        return render(request=request, template_name="category.html", context=context)


class GpuView(View):
    """ Displays only products in GPU category(id=2) """

    def get(self, request):
        form = Product.objects.filter(category_id='2')
        context = {
            'form': form
        }
        return render(request=request, template_name="category.html", context=context)


class MotherboardView(View):
    """ Displays only products in Motherboards category(id=3) """

    def get(self, request):
        form = Product.objects.filter(category_id='3')
        context = {
            'form': form
        }
        return render(request=request, template_name="category.html", context=context)


class ProductView(View):
    """ Displays product details - specification, price, etc. """

    def get(self, request, product):
        form = Product.objects.filter(product=product)
        context = {
            'form': form
        }
        return render(request=request, template_name="product.html", context=context)


class UpdateUserView(View):
    """ DO POPRAWY """

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