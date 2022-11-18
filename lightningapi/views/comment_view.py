"""View module for handling requests for comment data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from lightningapi.models import Comment, RareUser, Post


class CommentView(ViewSet):
    """Lightning Raccoons API comments view"""

    def list(self, request):
        comments = Comment.objects.all()
        serialized = CommentSerializer(comments, many=True)
        return Response(serialized.data)

    def create(self, request):
        author = RareUser.objects.get(pk=request.data["user"])
        post = Post.objects.get(pk=request.data["post"])

        comment = Comment.objects.create(
            author=author,
            post=post,
            content=request.data["content"]
        )
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def update(self, request, pk):
        editing_comment = Comment.objects.get(pk=pk)
        editing_comment.content = request.data["content"]

        return Response(None, status=status.HTTP_205_RESET_CONTENT)

    def destroy(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        comment.delete()

        return Response(None, status=status.HTTP_204_NO_CONTENT)


class CommentSerializer(serializers.ModelSerializer):
    """JSON serializer for comments"""
    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'content')
