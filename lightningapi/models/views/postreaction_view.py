"""View module for handling requests for postreaction data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from lightningapi.models import PostReaction


class PostReactionView(ViewSet):
    """Lightning Raccoons API postreaction view"""

    def list(self, request):
        """Handle GET requests to get all postreactions

        Returns:
            Response -- JSON serialized list of postreactions
        """

        postreactions = PostReaction.objects.all()
        serialized = PostReactionSerializer(postreactions, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single postreaction

        Returns:
            Response -- JSON serialized postreaction record
        """

        postreaction = PostReaction.objects.get(pk=pk)
        serialized = PostReactionSerializer(
            postreaction, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)


class PostReactionSerializer(serializers.ModelSerializer):
    """JSON serializer for postreactions"""
    class Meta:
        model = PostReaction
        fields = ('id', 'reaction', 'user', 'post')
