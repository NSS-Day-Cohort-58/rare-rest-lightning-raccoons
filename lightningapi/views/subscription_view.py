"""View module for handling requests for subscription data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from lightningapi.models import Subscription


class SubscriptionView(ViewSet):
    """Lighting Raccoons API subscription view"""

    def list(self, request):
        """Handle GET requests to get all subscriptions

        Returns:
            Response -- JSON serialized list of subscriptions
        """

        subscriptions = Subscription.objects.all()
        serialized = SubscriptionSerializer(subscriptions, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single subscription

        Returns:
            Response -- JSON serialized subscription record
        """

        subscription = Subscription.objects.get(pk=pk)
        serialized = SubscriptionSerializer(
            subscription, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)


class SubscriptionSerializer(serializers.ModelSerializer):
    """JSON serializer for subscription"""
    class Meta:
        model = Subscription
        fields = ('id', 'follower', 'author', 'created_on')
