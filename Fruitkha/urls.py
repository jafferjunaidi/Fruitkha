"""
URL configuration for Fruitkha project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from Fruitkha import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    # path('about/', views.about , name="about"), # name route
    path('about/', views.about), 
    path('news/', views.news), 
    path('grapes_news/', views.grapes), 
    path('fruits_table_news/', views.fruits_table), 
    path('fruits_stall_news/', views.fruits_stall), 
    path('fruits_plate_news/', views.fruits_plate), 
    path('fruits_bucket_news/', views.fruits_bucket), 
    path('celeb_straw_news/', views.celeb_straw),     
    path('contact/', views.contact), 
    path('shop/', views.shop), 
    path('singlepage_apple/', views.singlepage_apple),
    path('singlepage_grapes/', views.singlepage_grapes),
    path('singlepage_kiwi/', views.singlepage_kiwi),
    path('singlepage_lemon/', views.singlepage_lemon),
    path('singlepage_rasp/', views.singlepage_rasp),
    path('singlepage_straw/', views.singlepage_straw), 
    path('cart/', views.cart),
    path('checkout/', views.checkout),
    path('error/', views.error404)
]