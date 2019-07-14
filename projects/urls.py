from django.urls import path
from . import views


urlpatterns = [
    path("", views.IndexView.as_view(), name="project_index"),
    path("<int:pk>/", views.DetailView.as_view(), name="project_detail"),
]
