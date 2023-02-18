from django.views.generic import DetailView, ListView

from blog.models import Blog


class BlogsListView(ListView):
    model = Blog


class BlogsDetailView(DetailView):
    model = Blog
