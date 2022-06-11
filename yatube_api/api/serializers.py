from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Group, Post, Follow, User


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор модели Post."""
    author = SlugRelatedField(slug_field='username',
                              read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор модели Group."""
    class Meta:
        model = Group
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор модели Comment."""
    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True)
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('author', 'post')


class FollowSerializer(serializers.ModelSerializer):
    """Сериализатор модели Follow."""
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Follow
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following',)
            )
        ]

    def validate(self, data):
        """Проверка подписки на самого себя."""
        if data['following'] == self.context['request'].user:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя!')
        return data
