from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from Univnet_Beta.forms import Student_SignUpForm
from Univnet_Beta.forms import Alumni_SignUpForm

# @login_required
def home(request):
    return render(request, 'home.html')


def student_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = Student_SignUpForm()
    return render(request, 'student_signup.html', {'form': form})


def alumni_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = Alumni_SignUpForm()
    return render(request, 'alumni_signup.html', {'form': form})


def handler400(request):
    response = render(request, '404.html', status=404)
    return response


def handler500(request):
    response = render(request, '500.html', status=500)
    response.status_code = 500
    return response
