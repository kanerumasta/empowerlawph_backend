from django.contrib import admin
from django.urls import path, include,re_path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="EmpowerLawPH API",
        default_version='v1',
        description="API documentation",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],

)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(
[
    path('auth/', include('accounts.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.urls')),
    path('search', include('search.urls')),
    path('cases/', include('case.urls'))
]
    )),
      path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
