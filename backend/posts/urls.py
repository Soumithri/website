from django.urls import path

from . import views

urlpatterns = [
    path('posts/', views.PostList.as_view(), name='posts'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='post-detail'),
    path('projects/', views.ProjectList.as_view(), name='projects'),
    path('project/<int:pk>/', views.ProjectDetail.as_view(), name='project-detail'),
    path('author/', views.AuthorDetail.as_view(), name='authorDetail'),
]
