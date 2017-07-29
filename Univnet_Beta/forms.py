from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Student_SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Required.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    bio = forms.CharField(max_length=1000, help_text='Say how awesome you are.')
    extra_curr = forms.CharField(max_length=1000, help_text='What are your extra curricular activities.')
    image = forms.ImageField( help_text='Maximum Resoluton : 400 * 400')
    cv_url = forms.CharField(max_length=1000, help_text='Provide the link to your CV.')
    year_of_study = forms.IntegerField()
    address = forms.CharField(max_length=1000,)
    experience = forms.CharField(max_length=1000, help_text='Your internship and/or research experience. Optional.')
    projects_info = forms.CharField(max_length=1000, help_text='Provide the link to your Projects. Optional.')
    publications = forms.CharField(max_length=1000, help_text='Provide the link to your Publications. Optional.')
    school_studied = forms.CharField(max_length=1000,)
    univ_studying = forms.CharField(max_length=1000, help_text='Where are you studying right now.')
    course_name = forms.CharField(max_length=1000, help_text='Your stream.')
    skills = forms.CharField(max_length=1000, help_text='Your skills.')
    interests = forms.CharField(max_length=1000, help_text='What are you interested in.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'bio','extra_curr','image','cv_url','year_of_study','address','experience','projects_info','publications','school_studied','univ_studying','course_name','skills','interests')


class Alumni_SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Required.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    bio = forms.CharField(max_length=1000, help_text='Say how awesome you are.')
    extra_curr = forms.CharField(max_length=1000, help_text='What are your extra curricular activities.')
    image = forms.ImageField( help_text='Maximum Resoluton : 400 * 400')
    cv_url = forms.CharField(max_length=1000, help_text='Provide the link to your CV.')
    position = forms.CharField(max_length=1000, help_text='Your current position (University/Job).')
    experience = forms.CharField(max_length=1000, help_text='Your internship and/or research experience.')
    projects_info = forms.CharField(max_length=1000, help_text='Provide the link to your Projects.')
    publications = forms.CharField(max_length=1000, help_text='Provide the link to your Publications.')
    school_studied = forms.CharField(max_length=1000,)
    work = forms.CharField(max_length=1000, help_text='Your domain of work.')
    univ_studied = forms.CharField(max_length=1000, help_text='Where did you study before.')
    skills = forms.CharField(max_length=1000, help_text='Your skills.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'bio','extra_curr','image','cv_url','position','experience','projects_info','publications','school_studied','work','univ_studied','skills',)