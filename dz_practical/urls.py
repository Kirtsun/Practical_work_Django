from django.urls import path
from . import views


urlpatterns = [
    path('new_post/', views.post_new, name='new_post'),
    path('<int:pk>/update/', views.UserPostUpdate.as_view(), name='update'),
    path('create_comment/<int:pk>/', views.create_comments, name='create_comments'),
    path('', views.PostList.as_view(), name='post'),
    path('author_post/<int:pk>/', views.author_post, name='author_post'),
    path('post_detail/<int:pk>/', views.detail_post, name='post_detail'),
    path('my_blanks/', views.MyBlanks.as_view(), name='my_blanks')

]
