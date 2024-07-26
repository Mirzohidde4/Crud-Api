from django.shortcuts import render
from .serializers import PostSerializer, UserSerializer
from .models import Posts
from rest_framework import generics, permissions, viewsets
from django.contrib.auth import get_user_model

# Create your views here.
class PostApi(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer


# class PostList(generics.ListCreateAPIView):
#     # permission_classes = (permissions.IsAuthenticated,)
#     queryset = Posts.objects.all()
#     serializer_class = PostSerializer


# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     # permission_classes = (permissions.IsAuthenticated,)
#     queryset = Posts.objects.all()
#     serializer_class = PostSerializer


class UserApi(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer 


# class UserList(generics.ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer    


# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
        