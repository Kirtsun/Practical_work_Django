from django.urls import path
from . import views

urlpatterns = [
    path('authorprofile/<int:pk>/', views.public_profile, name='public_profile'),
    path('my_profile/', views.my_profile, name='my_profile')
]