from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Tennis Analysis System",
        default_version='v1',
        description="Tennis Analysis System API Documentation",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = (
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-redoc'),
    # path('api/', include('matches.urls')),
    path('api/accounts/', include('accounts.urls')),
)
