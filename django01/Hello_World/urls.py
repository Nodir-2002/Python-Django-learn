from django.conf.urls import url
from django.urls import path
from .views import Hello


urlpatterns = [
    path('',Hello,name='Hello')
]
