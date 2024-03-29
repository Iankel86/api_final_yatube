from rest_framework import filters, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

from .mixins import CreateDestroyListViewSet
from .permissions import IsAuthorOrReadOnly
from .serializers import (CommentSerializer, GroupSerializer,
                          PostSerializer, FollowSerializer)
from posts.models import Group, Post


class PostViewSet(viewsets.ModelViewSet):
    """
    Дает работать с постами.
    Имеет тип доступа: чтение/авторизация
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly, )
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Дает работать с группами пользователей.
    Имеет тип доступа: только чтение
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,
                          IsAuthorOrReadOnly]
    pagination_class = None


class CommentViewSet(viewsets.ModelViewSet):
    """
    Дает работать с комментариями пользователей.
    Имеет тип доступа: чтение/авторизация
    """
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly, )
    pagination_class = None

    def get_post(self):
        return get_object_or_404(Post, id=self.kwargs.get("post_id"))

    def get_queryset(self):
        return self.get_post().comments.all()

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user, post=self.get_post(),)


class FollowViewSet(CreateDestroyListViewSet):
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated, ]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)
    pagination_class = None

    def get_queryset(self):
        return self.request.user.follower

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
