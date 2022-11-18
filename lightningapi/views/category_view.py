"""View module for handling requests for customer data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from lightningapi.models import Category, RareUser


class CategoryView(ViewSet):
    """Lightning Raccoons API category view"""

    def list(self, request):
        """Handle GET requests to get all category

        Returns:
            Response -- JSON serialized list of categories
        """

        categories = Category.objects.all()
        serialized = CategorySerializer(categories, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single category

        Returns:
            Response -- JSON serialized category record
        """

        category = Category.objects.get(pk=pk)
        serialized = CategorySerializer(category, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)

    def create(self, request):
        """ Handles POST operations

        Returns
            Response -- JSON serialized category instance
        """
        # Getting the user that is logged in
        user = RareUser.objects.get(user=request.auth.user)

        # Creating a new category
        category = Category.objects.create(
            label=request.data['label'],
        )
        serializer = CategorySerializer(category)
        return Response(serializer.data)


class CategorySerializer(serializers.ModelSerializer):
    """JSON serializer for categories"""
    class Meta:
        model = Category
        fields = ('id', 'label')
