from django.views import generic
from django.shortcuts import get_object_or_404
from blog.models import Post, Comment


class IndexView(generic.ListView):
    template_name = 'blog/blog_index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        """Return the last five published questions."""
        return Post.objects.all().order_by('-created_on')


class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/blog_detail.html'

    def get_context_data(self, **kwargs):
        post = Post.objects.get(pk=self.kwargs['pk'])
        comments = Comment.objects.filter(post=post)
        context = {
            'post': post,
            'comments': comments
        }
        return context


class CategoryView(generic.DetailView):
    model = Post
    template_name = 'blog/blog_category.html'

    def get_context_data(self, **kwargs):
        posts = Post.objects.filter(
            categories__name__contains=self.kwargs['category']
        ).order_by(
            '-created_on'
        )
        context = {
            "category": self.kwargs['category'],
            "posts": posts
        }
        return context



