
from django.contrib import admin
from django.urls import path, include

from finance.views import (IndexView, OrganizationListView, OrganizationDetailView,
                           OrganizationCreateView, OrganizationUpdateView, OrganizationDeleteView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('', IndexView.as_view(), name='index'),
    path('organizations', OrganizationListView.as_view(), name='organizations'),
    path('organizations/detail/<int:pk>', OrganizationDetailView.as_view(), name='organization_detail'),
    path('organizations/create/', OrganizationCreateView.as_view(), name='organization_create'),
    path('organizations/edit/<int:pk>', OrganizationUpdateView.as_view(), name='organization_update'),
    path('organizations/delete/<int:pk>', OrganizationDeleteView.as_view(), name='organization_delete'),
]
