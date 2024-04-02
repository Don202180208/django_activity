from django.contrib import admin
from .models import College, Program, Organization, Student, OrgMember

admin.site.register(College)
admin.site.register(Program)
admin.site.register(Organization)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_id", "lastname", "firstname", "middlename", "program")
    search_fields = ("lastname", "firstname",)

@admin.register(OrgMember)
class OrgMemberAdmin(admin.ModelAdmin):
    list_display = ("get_lastname", "get_firstname", "get_middlename", "get_program")
    search_fields = ("student__lastname", "student__firstname",)

    def get_lastname(self, obj):
        return obj.student.lastname

    def get_firstname(self, obj):
        return obj.student.firstname

    def get_middlename(self, obj):
        return obj.student.middlename

    def get_program(self, obj):
        return obj.student.program

    get_lastname.short_description = "Last Name"
    get_firstname.short_description = "First Name"
    get_middlename.short_description = "Middle Name"
    get_program.short_description = "Program"

# Register your models here.
