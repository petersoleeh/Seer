from django.urls import path
from . import views


urlpatterns = [

    # the landing url
    path('', views.index, name='index'),
]
