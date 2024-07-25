from django.shortcuts import render
from .serializers import PostSerializer
from .models import Posts
from rest_framework import generics, permissions

# Create your views here.
class PostList(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Posts.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Posts.objects.all()
    serializer_class = PostSerializer