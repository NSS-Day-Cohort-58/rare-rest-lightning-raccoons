"""View module for handling requests for user data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from lightningapi.models import RareUser


class RareUserView(ViewSet):
    """Lightning Raccoons API users view"""

    def list(self, request):
        """Handle GET requests to get all users

        Returns:
            Response -- JSON serialized list of users
        """

        users = RareUser.objects.all()
        serialized = RareUserSerializer(users, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single user

        Returns:
            Response -- JSON serialized user record
        """

        user = RareUser.objects.get(pk=pk)
        serialized = RareUserSerializer(user, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)


class RareUserSerializer(serializers.ModelSerializer):
    """JSON serializer for users"""
    class Meta:
        model = RareUser
        fields = ('id', 'firstName', 'lastName', 'email', 'bio', 'username',
                  'password', 'profileImageURL', 'createdOn', 'active')
