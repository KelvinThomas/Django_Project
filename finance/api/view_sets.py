from rest_framework.viewsets import ModelViewSet

from finance.api.serializers import OrganizationSerializer
from finance.models import Organization


class OrganizationViewSet(ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer