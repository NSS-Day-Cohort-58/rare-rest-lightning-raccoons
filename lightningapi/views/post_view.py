from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from lightningapi.models import Post
from lightningapi.models import Category
from lightningapi.models import RareUser


class PostView(ViewSet):
    def retrieve(self, request, pk):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def list(self, request):
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized Post instance
        """
        user = RareUser.objects.get(pk=request.data["user"])
        category = Category.objects.get(pk=request.data["category"])
        
        post = Post.objects.create(
            user = user,
            category = category,
            title = request.data["title"],
            publication_date = request.data["publication_date"],
            image=request.data["image"],
            content=request.data["content"],
            approved = request.data["approved"]
        )
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """Handle PUT requests for a Post

        Returns:
            Response -- Empty body with 204 status code
        """
        
        editing_post = Post.objects.get(pk=pk)
        editing_post.category = Category.objects.get(pk=request.data["category"])
        editing_post.title = request.data["title"]
        editing_post.image=request.data["image"]
        editing_post.content=request.data["content"]
        editing_post.approved = request.data["approved"]
        editing_post.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class PostSerializer(serializers.ModelSerializer):
    """JSON serializer for Post types
    """
    class Meta:
        model = Post
        fields = ('id', 'category', 'title', 'publication_date','image','content','approved')
        depth = 2
