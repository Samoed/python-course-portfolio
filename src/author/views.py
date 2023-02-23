from django.views.generic import DetailView, ListView

from author.models import Author


class AuthorListView(ListView):
    model = Author


class AutorDetailView(DetailView):
    model = Author
