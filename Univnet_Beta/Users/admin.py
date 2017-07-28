from django.contrib import admin
from .models import CourseIn, Departments, Interests, Alumni, Student

admin.site.register(CourseIn)
admin.site.register(Departments)
admin.site.register(Interests)
admin.site.register(Alumni)
admin.site.register(Student)
