from django.urls import path
from .views import RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
]
# This file defines the URL patterns for the user registration endpoint in the Forex School application.
# It includes a single path for user registration that maps to the RegisterView.