from django.urls import path 
from . import views 

urlpatterns = [
    path("", views.index, name="index"),
    path("bilal", views.bilal, name="bilal"), 
    path("<str:name>", views.greet, name="greet")
]
