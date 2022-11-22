from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from lightningapi.models import Post, Tag
from django.contrib.auth.models import User


class PostTagView(ViewSet):

    def create(self, request):
        """Handle POST operations
            Returns
                Response -- JSON serialized post_tag instance
            """
        user = RareUser.objects.get(pk=request.data["user"])
        post_tag = PostTag.objects.get(pk=request.data["post_tag"])

        post = Post.objects.create(
            user=user,
            post_tag=post_tag,

        )
        serializer = PostTagSerializer(post_tag)
        return Response(serializer.data)
