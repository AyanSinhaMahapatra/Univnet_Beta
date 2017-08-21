from django.shortcuts import render, get_object_or_404
from Users.models import Student,Alumni

# Create your views here.
def find_student(request):
    all_students = Student.objects.all()
    return render(request, 'Find_student.html', {'all_students': all_students, })

