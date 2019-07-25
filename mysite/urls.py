from django.urls import path
from . import views


urlpatterns = [
    path("", views.HomePageView.as_view(), name='home'),
    path("project/<int:pk>", views.ProjectDetailView.as_view(), name='project_detail'),
    path("underconstruction/", views.UnderConstructionView.as_view(), name='under_construction'),
]
