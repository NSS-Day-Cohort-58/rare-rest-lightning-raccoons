"""lightningraccoons URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from rest_framework import routers
from django.urls import path
from lightningapi.views import register_user, login_user, CategoryView, CommentView, PostView, PostReaction
from lightningapi.views import SubscriptionView, TagView, RareUserView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'categories', CategoryView, 'category')
router.register(r'comments', CommentView, 'comment')
router.register(r'posts', PostView, 'post')
# router.register(r'reactions', PostReaction, 'reaction')
router.register(r'subscriptions', SubscriptionView, 'subscription')
router.register(r'tags', TagView, 'tag')
router.register(r'rare_users', RareUserView, 'rare_user')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
