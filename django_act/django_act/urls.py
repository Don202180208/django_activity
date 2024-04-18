"""
URL configuration for django_act project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from studentorg.views import HomePageView, OrganizationList, OrganizationCreateView, OrganizationUpdateView, OrganizationDeleteView
from django.contrib.auth import views as auth_views
from django.urls import path, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name="home"),
    path('organization_list', OrganizationList.as_view(), name="organization-list"),
    path('organization_list/add', OrganizationCreateView.as_view(), name="organization-add"),
    path('organization_list/<pk>', OrganizationUpdateView.as_view(), name="organization-update"),
    path('organization_list/<pk>/delete', OrganizationDeleteView.as_view(), name="organization-delete"),
    re_path(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    re_path(r"^logout/$", auth_views.LogoutView.as_view(), name="logout"),
]
