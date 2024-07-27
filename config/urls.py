from django.contrib import admin
from django.urls import path, include, re_path
from .sxema import schema_view


urlpatterns = [
    path('admin/', admin.site.urls),
    # apps
    path('api/', include('posts.urls')),
    # api
    path('api-auth/', include('rest_framework.urls')),
    path('api/rest-auth/', include('dj_rest_auth.urls')),
    path('api/rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    # swagger
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
