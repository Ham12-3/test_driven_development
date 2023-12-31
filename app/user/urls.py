"""
URL mappins for the USER API.
"""

from django.urls import path
from user import views


app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('validate-email/', views.EmailValidationView.as_view(),
         name='validate-email'),

]
