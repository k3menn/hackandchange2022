from django.urls import path
from .views import *

urlpatterns = [
    path('', General.base , name = "base"),
    path('r/',Authorization.aut , name = 'log'),
    path('register/', Registration.Register, name='account'),
]
