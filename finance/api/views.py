from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from finance.models import Organization
from finance.api.serializers import OrganizationSerializer


class OrganizationListAPIView(ListAPIView):
    """This api allows users to list all organizations"""
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class OrginizationCreateAPIView(CreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class OrganizationDetailAPIView(RetrieveAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class OrganizationUpdateAPIView(UpdateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class OrganizationDeleteAPIView(DestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
