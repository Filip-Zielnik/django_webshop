from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import redirect, render
from django.views import View

from .forms import LoginForm, UserForm, ProfileForm
from .models import Address, Product, Profile


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


class UpdateUserView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user_form = UserForm
        profile_form = ProfileForm
        context = {
            'user_form': user_form,
            'profile_form': profile_form,
        }
        return render(request=request, template_name="update_user.html", context=context)

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
            return render(request=request, template_name="update_user.html", context=context)
        return render(request=request, template_name="update_user.html")


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
                return redirect('home')
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


# class LoggedView(LoginRequiredMixin, View):
#     """ ROBOCZY WIDOK ŻEBY WYFILTROWAĆ ADRESY DANEGO UŻYTKOWNIKA """
#
#     login_url = '/login/'
#
#     def get(self, request, user_id, *args, **kwargs):
#         profile = Profile.objects.get(user_id=user_id)
#         form = Address.objects.filter(profile=profile)
#         context = {
#             'form': form,
#             'profile': profile,
#         }
#         return render(request=request, template_name="logged.html", context=context)

class LoggedView(LoginRequiredMixin, View):
    """ View ONLY available for logged users """

    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        form = Address.objects.all()
        context = {
            'form': form,
        }
        return render(request=request, template_name="logged.html", context=context)


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

    def get(self, request, product, *args, **kwargs):
        form = Product.objects.filter(product=product)
        context = {
            'form': form
        }
        return render(request=request, template_name="product.html", context=context)


class AddressView(LoginRequiredMixin, View):
    """ Displays detailed information about address such as country, city, ect. """

    login_url = '/login/'

    def get(self, request, address, *args, **kwargs):
        form = Address.objects.filter(name=address)
        context = {
            'form': form
        }
        return render(request=request, template_name="address.html", context=context)
