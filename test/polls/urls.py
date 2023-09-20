from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    
    # ex: /polls/login
    path('login/',views.login, name="login"),
    
]