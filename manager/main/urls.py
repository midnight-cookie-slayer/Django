from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-me', views.about),
    path('registration', views.register, name='register'),
    path('log_in', views.user_login, name='log_in'),
    path('log_out', views.log_out, name='log_out'),
]



