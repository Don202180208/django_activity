from django.shortcuts import render, redirect, get_object_or_404
from typing import Any
from django.db.models.query import QuerySet
from django.db.models import Q
from django.views.generic.list import ListView
from studentorg.models import Organization
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from studentorg.forms import OrganizationForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(login_required, name='dispatch')

class HomePageView(ListView):
    model = Organization
    context_object_name = "home"
    template_name = "home.html"

class OrganizationList(ListView):
    model = Organization
    context_object_name = "organization"
    template_name = "org_list.html"
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        qs = super(OrganizationList, self).get_queryset(*args, **kwargs)
        if self.request.GET.get('q') != None:
            query = self.request.GET.get('q')
            qs = qs.filter(Q(name__icontains=query)) | (Q(description__icontains=query))
        return qs

class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = "org_add.html"
    success_url = reverse_lazy("organization-list")

class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = "org_edit.html"
    success_url = reverse_lazy("organization-list")


class OrganizationDeleteView(DeleteView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_del.html'
    success_url = reverse_lazy('organization-list')

# Create your views here.
