"""Health URL Configuration

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
from firstpage import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('diabetes',views.diabetes,name='diabetes'),
    path('predictdiabetes',views.predictdiabetes,name='predictdiabetes'),
    path('heart',views.heart,name='heart'),
    path('predictheart',views.predictheart,name='predictheart'),
    path('liver',views.liver,name='liver'),
    path('predictliver',views.predictliver,name='predictliver'),
    path('cancer',views.cancer,name='cancer'),
    path('predcancer',views.predcancer,name='predcancer'),
    path('kidney',views.kidney,name='kidney'),
    path('predictkidney',views.predictkidney,name='predictkidney'),
    path('enquire',views.enquire,name='enquire'),
    path('enquiredata',views.enquiredata,name='enquiredata'),
    path('bmi',views.bmi,name='bmi'),
    path('predictbmi',views.predictbmi,name='predictbmi'),
]
