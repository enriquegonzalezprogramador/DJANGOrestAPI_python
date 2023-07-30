
from django.urls import path

from medicines.views import medicines

from medicines.views import detail_medicine

urlpatterns = [
    path('', medicines),
    path('/<int:pk>', detail_medicine),
]