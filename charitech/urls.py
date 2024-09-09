
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularSwaggerView, SpectacularRedocView, SpectacularAPIView
from rest_framework.routers import DefaultRouter

from finance.api.view_sets import OrganizationViewSet
from finance.views import (IndexView, OrganizationListView, OrganizationDetailView,
                           OrganizationCreateView, OrganizationUpdateView, OrganizationDeleteView)
from finance.api.views import OrganizationListAPIView, OrganizationDetailAPIView, OrginizationCreateAPIView, \
    OrganizationDeleteAPIView, OrganizationUpdateAPIView

router = DefaultRouter()
router.register('organizations', OrganizationViewSet, basename='organizations')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('api-auth/', include('rest_framework.urls')),

    path('', IndexView.as_view(), name='index'),
    path('organizations', OrganizationListView.as_view(), name='organizations'),
    path('organizations/detail/<int:pk>', OrganizationDetailView.as_view(), name='organization_detail'),
    path('organizations/create', OrganizationCreateView.as_view(), name='organization_create'),
    path('organizations/edit/<int:pk>', OrganizationUpdateView.as_view(), name='organization_update'),
    path('organizations/delete/<int:pk>', OrganizationDeleteView.as_view(), name='organization_delete'),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api/v1/', include(router.urls))
    # path('api/v1/organizations', OrganizationListAPIView.as_view(), name='organizations_list'),
    # path('api/v1/organization/details/<int:pk>', OrganizationDetailAPIView.as_view(), name='organization_details'),
    # path('api/v1/organizations/create', OrginizationCreateAPIView.as_view(), name='organization_create'),
    # path('api/v1/organizations/delete/<int:pk>', OrganizationDeleteAPIView.as_view(), name='organization_delete'),
    # path('api/v1/organizations/update/<int:pk>', OrganizationUpdateAPIView.as_view(), name='organization_update'),

]
