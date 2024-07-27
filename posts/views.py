from django.shortcuts import render
from .serializers import PostSerializer, UserSerializer
from .models import Posts
from rest_framework import generics, permissions, viewsets
from django.contrib.auth import get_user_model
from rest_framework.pagination import PageNumberPagination

# Create your views here.
class LargePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class StandardPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 5


class PostApi(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    # pagination_class = StandardPagination


class UserApi(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer   
    pagination_class = LargePagination  


# class PostList(generics.ListCreateAPIView):
#     # permission_classes = (permissions.IsAuthenticated,)
#     queryset = Posts.objects.all()
#     serializer_class = PostSerializer


# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     # permission_classes = (permissions.IsAuthenticated,)
#     queryset = Posts.objects.all()
#     serializer_class = PostSerializer



# class UserList(generics.ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer    


# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
        