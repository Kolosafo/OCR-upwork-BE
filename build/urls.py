from django.urls import path
from . import views


urlpatterns = [
    path('',  views.main, name="main"),
    path('<str:id>/',  views.main, name="main"),
]
