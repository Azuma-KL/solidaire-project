from django.urls import path
from solidaire_api.comment.views import CommentCreateView, CommentRetriveUpdateDestroyView

urlpatterns = [
    path("", CommentCreateView.as_view()),
    path("<uuid:uuid>/", CommentRetriveUpdateDestroyView.as_view(lookup_field="uuid")),
    path("<int:pk>/", CommentRetriveUpdateDestroyView.as_view()),
]
