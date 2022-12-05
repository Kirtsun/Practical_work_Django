from django.urls import path
from . import views


urlpatterns = [
    path('new_post/', views.post_new, name='new_post'),
    path('<int:pk>/update/', views.UserPostUpdate.as_view(), name='update')
]
