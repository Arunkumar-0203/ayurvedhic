"""ayurvedhic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from ayurvedhic import settings
from ayurvedhic_app import admin_urls,Pharmacy_urls,doctor_urls,staff_urls,user_urls

from ayurvedhic_app.views import index_view, docters_view, login_view, registration_view, pharmacy_registration_view, \
    staff_registration_view, doctor_registration_view, user_registration_view, about_view, gallery_view

urlpatterns = [
    path('', index_view.as_view()),
    path('docters_view',docters_view.as_view()),
    path('login_view',login_view.as_view()),
    path('registration_view',registration_view.as_view()),
    path('user_registration_view',user_registration_view.as_view()),
    path('doctor_registration_view',doctor_registration_view.as_view()),
    path('staff_registration_view',staff_registration_view.as_view()),
    path('pharmacy_registration_view',pharmacy_registration_view.as_view()),
    path('admin/',admin_urls.urls()),
    path('Pharmacy/',Pharmacy_urls.urls()),
    path('doctor/',doctor_urls.urls()),
    path('staff/',staff_urls.urls()),
    path('user/',user_urls.urls()),
    path('about_view',about_view.as_view()),
    path('gallery_view',gallery_view.as_view()),

]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
