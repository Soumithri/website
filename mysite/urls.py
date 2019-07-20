from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    re_path(r'^project/(?P<pk>\d+)$', views.ProjectDetailView.as_view(), name='project_detail'),
]
