from rest_framework import serializers
from solidaire_content.models import Comment
from solidaire_api.user.serializers import UserPublicSerializer
from solidaire_api.post.querysets import PUBLIC_POSTS_QUERYSET

class CommentSerializer(serializers.ModelSerializer):
    
    owner = UserPublicSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = [
            "uuid",
            "owner",
            "body",
            "created_at",
        ]
        read_only_fields = [
            "uuid",
            "owner",
            "created_at"
        ]
    
class CommentCreateSerializer(serializers.Serializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    post = serializers.SlugRelatedField(slug_field="uuid", queryset=PUBLIC_POSTS_QUERYSET)
    body = serializers.CharField()