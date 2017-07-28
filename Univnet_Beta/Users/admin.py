from django.contrib import admin
from .models import Course, Department, Interest, Alumni, Student

admin.site.register(Course)
admin.site.register(Department)
admin.site.register(Interest)
admin.site.register(Alumni)
admin.site.register(Student)
