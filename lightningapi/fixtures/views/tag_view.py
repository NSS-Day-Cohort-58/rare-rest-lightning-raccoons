"""View module for handling requests for tag data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from lightningapi.models import Tag


class TagView(ViewSet):
    """Lighting Raccoons API tag view"""

    def list(self, request):
        """Handle GET requests to get all tags

        Returns:
            Response -- JSON serialized list of tags
        """

        tags = Tag.objects.all()
        serialized = TagSerializer(tags, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single tag

        Returns:
            Response -- JSON serialized tag record
        """

        tag = Tag.objects.get(pk=pk)
        serialized = TagSerializer(tag, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)


class TagSerializer(serializers.ModelSerializer):
    """JSON serializer for tags"""
    class Meta:
        model = Tag
        fields = ('id', 'label')
