
from django.urls import path
from .views import nuevohello

urlpatterns = [
    path('hello', nuevohello),
]
