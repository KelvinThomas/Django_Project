from django import forms
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy

from finance.models import Organization
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Div, Field, ButtonHolder, Submit, Button


class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['name', 'address', 'usertype']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('organization_create')
        self.helper.layout = Layout(
            Row(
                Div(
                    Column('name'),
                    css_class='col-md-6'
                ),
                Div(
                    Column('address'),
                    css_class='col-md-6'
                ),
                Div(
                    Field('usertype'),
                    css_class='col-md-3'
                ),
                ButtonHolder(
                    Submit('submit', 'Submit', css_class=''),
                    Button('cancel', 'Cancel', css_class='btn btn-danger')
                )
            )
        )

    def clean_address(self):
        address = self.cleaned_data['address']
        if 'P.O' not in address[0:3]:
            raise ValidationError('Address must begin with P.O')
        else:
            address = address
        return address

