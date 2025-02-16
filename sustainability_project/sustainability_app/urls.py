from django.urls import path
from .views import list_actions, create_action, remove_action

urlpatterns = [
    path("actions/", list_actions, name="list-actions"),  # Correct path
    path("actions/add/", create_action, name="add-action"),
    path("actions/delete/<int:action_id>/", remove_action, name="delete-action"),
]
