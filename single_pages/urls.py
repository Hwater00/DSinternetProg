from django.urls import path
from . import views

urlpatterns = [
    path('my_information/', views.my_information),
    path('about_me/', views.about_me),
    path('', views.landing),

]