from django.views.generic import ListView, DetailView
from mysite.models import Project


class HomePageView(ListView):
    model = Project
    template_name = 'mysite/home.html'


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'mysite/project_detail.html'
