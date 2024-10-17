from rest_framework import serializers
from solidaire_content.models import Comment
from solidaire_api.user.serializers import UserPublicSerializer

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
    
    