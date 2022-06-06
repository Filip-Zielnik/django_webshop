"""webshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from webshop_app.views import \
    HomeView, \
    LoginView, \
    RegistrationView, \
    LogoutView, \
    LoggedView, \
    CpuView, \
    GpuView, \
    MotherboardView, \
    UpdateUserView, \
    ProductView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name="home"),
    path('home/', HomeView.as_view(), name="home1"),
    path('login/', LoginView.as_view(), name="login"),
    path('registration/', RegistrationView.as_view(), name="registration"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('logged/', LoggedView.as_view(), name="logged"),
    path('category/cpu/', CpuView.as_view(), name="category-cpu"),
    path('category/gpu/', GpuView.as_view(), name="category-gpu"),
    path('category/motherboards/', MotherboardView.as_view(), name="category-motherboard"),
    path('update/', UpdateUserView.as_view(), name="update-user"),
    path('<product>/', ProductView.as_view(), name="product-view")
]
