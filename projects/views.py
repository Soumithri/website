from projects.models import Project
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'projects/project_index.html'
    context_object_name = 'projects'

    def get_queryset(self):
        """Return the last five published questions."""
        return Project.objects.all


class DetailView(generic.DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
