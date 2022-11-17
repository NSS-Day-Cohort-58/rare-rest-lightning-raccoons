"""View module for handling requests for post data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from lightningapi.models import Post


class PostView(ViewSet):
    """Lighting Raccoon API post view"""

    def list(self, request):
        """Handle GET requests to get all Posts

        Returns:
            Response -- JSON serialized list of Posts
        """

        posts = Post.objects.all()
        serialized = PostSerializer(posts, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single post

        Returns:
            Response -- JSON serialized post record
        """

        post = Post.objects.get(pk=pk)
        serialized = PostSerializer(post, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)


class PostSerializer(serializers.ModelSerializer):
    """JSON serializer for posts"""
    class Meta:
        model = Post
        fields = ('id', 'userId', 'categoryId', 'title',
                  'publicationDate', 'imageURL', 'content', 'approved')
