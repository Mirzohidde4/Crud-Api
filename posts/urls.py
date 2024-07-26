from django.urls import path
from .views import ( 
    # PostList, 
    # PostDetail, 
    # UserList, 
    # UserDetail, 
    PostApi,
    UserApi
)
from rest_framework.routers import   DefaultRouter 
from .serializers import UserSerializer

router = DefaultRouter()
router.register(r'users', UserApi, basename='users')


urlpatterns = [
    path('', PostApi.as_view({'get': 'list', 'post': 'create'})),
    path('<int:pk>/', PostApi.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('users/', UserApi.as_view({'get': 'list', 'post': 'create'})),
    path('users/<int:pk>/', UserApi.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]
