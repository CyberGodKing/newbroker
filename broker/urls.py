"""
URL configuration for broker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from webbroker import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name="home" ),
    path('faq/', views.faq, name="faq" ),
    path('term&conditions/', views.terms, name="terms" ),
    path('academy/', views.academy, name="academy" ),
    path('account/login/', views.loginuser, name="login" ),
    path('account/signup/', views.signup, name="signup" ),
    path('account/logout/', views.log_out, name="logout" ),
    path('account/password/', views.reset, name="reset" ),
    path('account/Dashboard/', views.dashboard, name="dashboard" ),
    path('account/profile/', views.profile, name="profile" ),
    path('account/packages/', views.plan, name="plan" ),
    path('account/deposit/', views.deposit, name="deposit" ),
    path('account/mypackages/', views.investment, name="investment" ),
    path('account/withdrawal/', views.withdraw, name="withdraw" ),
    path('account/history/', views.history, name="history" ),
    path('account/downline/', views.downline, name="downline" ),
]
