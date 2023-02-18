from django.urls import path

from author.views import AuthorListView, AutorDetailView

urlpatterns = [
    path("", AuthorListView.as_view(), name="authors"),
    path("<int:pk>/", AutorDetailView.as_view(), name="author"),
]
