
from django.urls import path
from myapp.views import *

urlpatterns = [
    path('', index),
    path('submit_form/', submit_form ),
    path('submissions/', submissions ),
]
