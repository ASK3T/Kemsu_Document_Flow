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
from django.urls import re_path, include

from .views import (
    RegistrationStudentAPIView, RegistrationStaffAPIView,
    BypassSheetsView, StudentList,
    LogoutView, RefreshTokenView,
    LoginView, BypassSheetView
)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('api/signup/student', RegistrationStudentAPIView.as_view(), name='user_registration'),
    path('api/signup/staff', RegistrationStaffAPIView.as_view(), name='staff_registration'),
    path('api/logout/', LogoutView.as_view(), name='auth_logout'),
    path('api/token/refresh/', RefreshTokenView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('api/users/<int:pk>/', StudentList.as_view(), name='student_list'),
    path('api/bypass_sheets/', BypassSheetsView.as_view(), name="bypass_sheets"),
    path('api/bypass_sheets/<int:pk>/', BypassSheetView.as_view(), name="bypass_sheet"),
    path('api/login/', LoginView.as_view(), name="login")
]