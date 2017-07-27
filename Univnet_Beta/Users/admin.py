from django.contrib import admin
from .models import course_in, departments, interests, alumni, student

admin.site.register(course_in)
admin.site.register(departments)
admin.site.register(interests)
admin.site.register(alumni)
admin.site.register(student)


# Register your models here.
