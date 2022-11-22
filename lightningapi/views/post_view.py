from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from lightningapi.models import Post
from lightningapi.models import Category
from lightningapi.models import RareUser, Tag
from django.contrib.auth.models import User
from rest_framework.decorators import action



class PostView(ViewSet):
    def retrieve(self, request, pk):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def list(self, request):
        posts = Post.objects.all()

        if "tag" in request.query_params:
            posts = Post.objects.filter(tags__in = request.query_params['tag'])
            
            

        # if "tag" in request.query_params:
        #     query_value = request.query_params['tag']
        #     posts = posts.filter(post.tag = query_value)
        
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized Post instance
        """
        user = RareUser.objects.get(pk=request.data["user"])
        category = Category.objects.get(pk=request.data["category"])

        post = Post.objects.create(
            user=user,
            category=category,
            title=request.data["title"],
            publication_date=request.data["publication_date"],
            image=request.data["image"],
            content=request.data["content"],
            approved=request.data["approved"]
        )
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a Post

        Returns:
            Response -- Empty body with 204 status code
        """

        editing_post = Post.objects.get(pk=pk)
        editing_post.category = Category.objects.get(
            pk=request.data["category"])
        editing_post.title = request.data["title"]
        editing_post.image = request.data["image"]
        editing_post.content = request.data["content"]
        editing_post.approved = request.data["approved"]
        editing_post.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    @action(methods=['post'], detail=True)
    def addTag(self, request, pk):
    
        tag = Tag.objects.get(pk=request.data["tag_id"])
        post = Post.objects.get(pk=request.data["post_id"])
        post.tags.add(tag)

        return Response({'message': 'Tag added'}, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

# class PostTagSerializer(serializers.ModelSerializer):

#     class Meta: Tag
#     fields = ('id', 'label', )

class PostSerializer(serializers.ModelSerializer):
    """JSON serializer for Post types
    """
    # tags = PostTagSerializer(many=True)

    class Meta:
        model = Post
        fields = ('id', 'user', 'category', 'title',
                  'publication_date', 'image', 'content', 'approved', 'tags', )
        depth = 2
        
