"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import re_path, include

from .views import RegistrationAPIView, RegistrationStaffAPIView
from .views import LoginAPIView
'''from djangoProject.views import RegisterEmployee, LoginView, ProfilePage, RegisterStudent
from djangoProject.views import HomeView, ContactsView, LoginView'''

'''path('accounts/login/', LoginView.as_view(), name="login"),
    path('accounts/profile/', ProfilePage.as_view(), name="profile"),
    path('admin/', admin.site.urls),
    path('accounts/register/employee', RegisterEmployee.as_view(), name="register_employee"),
    path('accounts/register/student', RegisterStudent.as_view(), name="register_student")'''

urlpatterns = [
    re_path('registration/user', RegistrationAPIView.as_view(), name='user_registration'),
    re_path('registration/staff', RegistrationStaffAPIView.as_view(), name='staff_registration'),
    re_path('login/', LoginAPIView.as_view(), name='user_login'),
]