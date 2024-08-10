from django.urls import path
from fruits.views import index

urlpatterns = [
    path('', index, name='index'),
]