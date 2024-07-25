from django.shortcuts import render
from .serializers import PostSerializer
from .models import Posts
from rest_framework import generics

# Create your views here.
class PostList(generics.ListAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer