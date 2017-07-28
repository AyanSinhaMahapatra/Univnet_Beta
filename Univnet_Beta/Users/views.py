from django.shortcuts import render, get_object_or_404

from .models import alumni,student

# Create your views here.



def details_stud(request,username_roll_request):
    stud_var = get_object_or_404(student ,username_roll =username_roll_request)

    return render(request, 'Users/details_student.html', {'student': stud_var})

def details_alumni(request,username_roll_request):
    alumni_var = get_object_or_404(alumni ,user_name =username_roll_request)

    return render(request, 'Users/details_alumni.html', {'alumni': alumni_var})