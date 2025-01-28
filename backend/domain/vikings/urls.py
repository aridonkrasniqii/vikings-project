from django.urls import path
from . import views

urlpatterns = [
    path('', views.vikings_list, name='vikings_list'),
]
