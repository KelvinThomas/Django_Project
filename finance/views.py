from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (TemplateView, ListView, DetailView, CreateView,
                                  UpdateView, DeleteView)
from finance.models import Organization
from finance.forms import OrganizationForm

# @login_required(login_url=reverse_lazy('login'))
# def index(request):
#     pass


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['organizations'] = Organization.objects.all().count()
        context['users'] = User.objects.all().count()
        return context

class OrganizationListView(LoginRequiredMixin, ListView):
    template_name = 'organization_list.html'
    model = Organization
    context_object_name = 'organizations'

    def get_queryset(self):
        qs = Organization.objects.all()
        return qs


class OrganizationDetailView(LoginRequiredMixin, DetailView):
    template_name = 'organization_detail.html'
    model = Organization
    context_object_name = 'org'

class OrganizationCreateView(LoginRequiredMixin, CreateView):
    template_name = 'organization_create.html'
    # model = Organization
    # fields = ['name', 'address']
    form_class = OrganizationForm
    success_url = reverse_lazy('organizations')

class OrganizationUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'organization_edit.html'
    model = Organization
    fields = ['name', 'address']
    success_url = reverse_lazy('organizations')


class OrganizationDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'organization_confirm_delete.html'
    model = Organization
    success_url = reverse_lazy('organizations')
