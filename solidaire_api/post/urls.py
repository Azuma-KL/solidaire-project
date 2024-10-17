from django.urls import path

from .views import (
    PostListCreateView,
    PostRetrieveView,
    PostMeListView,
    PostMeRetrieveUpdateDestroyView,
)

from solidaire_api.comment.views import _____

urlpatterns = [
    path("", PostListCreateView.as_view()),
    path("me/", PostMeListView.as_view()),
    path("<uuid:uuid>/", PostRetrieveView.as_view(lookup_field="uuid")),
    path("<int:pk>/", PostRetrieveView.as_view()),
    path("me/<uuid:uuid>/", PostMeRetrieveUpdateDestroyView.as_view(lookup_field="uuid")),
    path("me/<int:pk>/", PostMeRetrieveUpdateDestroyView.as_view()),
    path("<uuid:uuid>/comment/", _____.as_view(lookup_field="uuid")),
    path("<int:pk>/comment/", _____.as_view()),
]
