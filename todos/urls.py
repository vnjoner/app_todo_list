from django.urls import path
from .views import ToDoListView, ToDoDetailView


urlpatterns = [
    path("", ToDoListView.as_view()),
    path("<uuid:pk>/", ToDoDetailView.as_view()),
]
