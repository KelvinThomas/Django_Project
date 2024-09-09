#
# class OrganizationForm(forms.ModelForm):
#     class Meta:
#         model = Organization
#         fields = ['name', 'address', 'usertype']
from rest_framework import serializers

from finance.models import Organization


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'
