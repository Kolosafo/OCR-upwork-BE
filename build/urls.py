from django.urls import path
from . import views


urlpatterns = [
    path('',  views.main, name="main"),
    path('<str:api_key>',  views.main, name="main"),
]
