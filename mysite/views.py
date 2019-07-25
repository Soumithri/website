from django.views.generic import ListView, DetailView
from .models import Project, Author


class HomePageView(ListView):
    model = Project
    template_name = "mysite/home.html"


class ProjectDetailView(DetailView):
    model = Project
    template_name = "mysite/project_detail.html"


class UnderConstructionView(ListView):
    model = Author
    template_name = "mysite/under_construction.html"
