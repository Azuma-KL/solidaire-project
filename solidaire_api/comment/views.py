from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.mixins import (
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from .querysets import ALL_COMMENTS_QUERYSET
from .serializers import CommentSerializer, CreateCommentSerializer

from solidaire_api.permissions import AllowAny, IsAuthenticated, IsCommentOrPostOwner
from solidaire_content.models import Comment
from solidaire_api.exceptions import BadRequest