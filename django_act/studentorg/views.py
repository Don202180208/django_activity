from django.shortcuts import render
from typing import Any
from django.db.models.query import QuerySet
from django.db.models import Q
from django.views.generic.list import ListView
from studentorg.models import Organization, OrgMember, Student, College, Program
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from studentorg.forms import OrganizationForm, OrgmemForm, StudentForm, CollegeForm, ProgramForm
from django.urls import reverse_lazy, path, re_path
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(login_required, name='dispatch')

class HomePageView(ListView):
    model = Organization
    context_object_name = "home"
    template_name = "home.html"

class OrgMemberList(ListView):
    model = OrgMember
    context_object_name = "org_members"
    template_name = "orgmemb_list.html"
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        qs = super(OrgMemberList, self).get_queryset(*args, **kwargs)
        if self.request.GET.get('q') != None:
            query = self.request.GET.get('q')
            qs = qs.filter(Q(student__firstname__icontains=query) | Q(organization__name__icontains=query) | Q(date_joined__icontains=query))
        return qs

class OrganizationList(ListView):
    model = Organization
    context_object_name = "organization"
    template_name = "org_list.html"
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        qs = super(OrganizationList, self).get_queryset(*args, **kwargs)
        if self.request.GET.get('q') != None:
            query = self.request.GET.get('q')
            qs = qs.filter(Q(name__icontains=query) | Q(description__icontains=query) | Q(college__college_name__icontains=query))
        return qs

class StudentList(ListView):
    model = Student
    context_object_name = "student"
    template_name = "student_list.html"
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        qs = super(StudentList, self).get_queryset(*args, **kwargs)
        if self.request.GET.get('q') != None:
            query = self.request.GET.get('q')
            qs = qs.filter(Q(lastname__icontains=query) | Q(firstname__icontains=query) | Q(program__prog_name__icontains=query))
        return qs

class CollegeList(ListView):
    model = College
    context_object_name = "college"
    template_name = "college_list.html"
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        qs = super(CollegeList, self).get_queryset(*args, **kwargs)
        if self.request.GET.get('q') != None:
            query = self.request.GET.get('q')
            qs = qs.filter(Q(college_name__icontains=query))
        return qs
    
class ProgramList(ListView):
    model = Program
    context_object_name = "program"
    template_name = "program_list.html"
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        qs = super(ProgramList, self).get_queryset(*args, **kwargs)
        if self.request.GET.get('q') != None:
            query = self.request.GET.get('q')
            qs = qs.filter(Q(prog_name__icontains=query) | Q(college__college_name__icontains=query))
        return qs

class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = "org_add.html"
    success_url = reverse_lazy("organization-list")

class OrgmemCreateView(CreateView):
    model = OrgMember
    form_class = OrgmemForm
    template_name = "orgmem_add.html"
    success_url = reverse_lazy("orgmember-list")

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = "student_add.html"
    success_url = reverse_lazy("student-list")

class CollegeCreateView(CreateView):
    model = College
    form_class = CollegeForm
    template_name = "college_add.html"
    success_url = reverse_lazy("college-list")

class ProgramCreateView(CreateView):
    model = Program
    form_class = ProgramForm
    template_name = "program_add.html"
    success_url = reverse_lazy("program-list")

class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = "org_edit.html"
    success_url = reverse_lazy("organization-list")

class OrgmemUpdateView(UpdateView):
    model = OrgMember
    form_class = OrgmemForm
    template_name = "orgmem_edit.html"
    success_url = reverse_lazy("orgmember-list")

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = "student_edit.html"
    success_url = reverse_lazy("student-list")

class CollegeUpdateView(UpdateView):
    model = College
    form_class = CollegeForm
    template_name = "college_edit.html"
    success_url = reverse_lazy("college-list")

class ProgramUpdateView(UpdateView):
    model = Program
    form_class = ProgramForm
    template_name = "program_edit.html"
    success_url = reverse_lazy("program-list")

class OrganizationDeleteView(DeleteView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_del.html'
    success_url = reverse_lazy('organization-list')

class OrgmemDeleteView(DeleteView):
    model = OrgMember
    form_class = OrgmemForm
    template_name = 'orgmem_del.html'
    success_url = reverse_lazy('orgmember-list')

class StudentDeleteView(DeleteView):
    model = Student
    form_class = StudentForm
    template_name = 'student_del.html'
    success_url = reverse_lazy('student-list')

class CollegeDeleteView(DeleteView):
    model = College
    form_class = CollegeForm
    template_name = 'college_del.html'
    success_url = reverse_lazy('college-list')

class ProgramDeleteView(DeleteView):
    model = Program
    form_class = ProgramForm
    template_name = 'program_del.html'
    success_url = reverse_lazy('program-list')
# Create your views here.
