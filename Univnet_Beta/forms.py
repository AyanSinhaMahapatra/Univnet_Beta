from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Users.models import Course, Level, Interest, University, Skill


class Student_SignUpForm(UserCreationForm, ModelForm):
    username_roll = forms.CharField(max_length=20, help_text=' Your Unique University Roll Number')
    email_id = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField( label='First Name', max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    phone_no = forms.IntegerField(max_value=9999999999)
    bio = forms.CharField(max_length=1000, help_text='Say how awesome you are.')
    extra_curr = forms.CharField(max_length=1000, help_text='What are your extra curricular activities.')
    image = forms.ImageField( help_text='Great if you can keep your face at the middle, and yes, has to be "Your Face"')
    cv_url = forms.CharField(max_length=1000, help_text='Provide the link to your CV.')
    year_of_study = forms.IntegerField()
    address = forms.CharField(max_length=1000)

    experience = forms.CharField(max_length=1000 ,help_text='Your internship and/or research experience. Mention Dates. Use Multiple Lines . If multiple Experiences use Ordered Lists . If none specify "None" ')
    projects_info = forms.CharField(max_length=1000,
        help_text='Provide the details your Projects. Mention Dates. Use Multiple Lines . If multiple Projects use Ordered Lists. If none specify "None"')
    publications = forms.CharField(max_length=1000,
        help_text='Provide the details of your Publications.  Mention Dates. Use Multiple Lines . If multiple Publications use Ordered Lists. If none specify "None"')
    school_studied = forms.CharField(max_length=1000,
        help_text='The Schools you Studied In. With Dates. If Multiple use Ordered Lists')

    univ_studying = forms.ModelChoiceField(queryset= University.objects.all(),help_text='The University you are studying right now.')
    course_name = forms.ModelChoiceField(queryset= Course.objects.all() ,help_text='Your stream.')
    level= forms.ModelChoiceField(queryset= Level.objects.all(), help_text='Level of Course Pursuing')
    work_field_main = forms.ModelChoiceField(queryset= Interest.objects.all() , help_text='What are you interested in pursuing as Research Topic/Projects. Basically why you came to this site.')


    skills = forms.ModelMultipleChoiceField(queryset= Skill.objects.all() , help_text='Your skills. Hold Ctrl to select Multiple')

    class Meta:
        model = User
        fields = ('username_roll', 'first_name', 'last_name', 'email', 'password',
                  'phone_no' , 'bio','extra_curr','image','cv_url','year_of_study',
                  'address','experience','projects_info','publications','school_studied',
                  'univ_studying','course_name','skills','work_field_main')


class Alumni_SignUpForm(UserCreationForm, ModelForm):
    username= forms.CharField(max_length=20, help_text= 'Your Unique Username')
    email_id = forms.EmailField(max_length=254, help_text='Inform a valid email address.')
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=30, required=False, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Required.')
    phone_no = forms.IntegerField(max_value=9999999999)
    bio = forms.CharField(max_length=1000, help_text='Say how awesome you are.')
    image = forms.ImageField( help_text='Great if you can keep your face at the middle, and yes, has to be "Your Face"')
    cv_url = forms.CharField(max_length=1000, help_text='Provide the link to your CV.')
    position = forms.CharField(max_length=1000, help_text='Your current position (University/Job).')

    experience = forms.CharField(max_length=1000, help_text='Your internship and/or research experience. Mention Dates. Use Multiple Lines . If multiple Experiences use Ordered Lists . If none specify "None" ')
    projects_info = forms.CharField(max_length=1000, help_text='Provide the details your Projects. Mention Dates. Use Multiple Lines . If multiple Projects use Ordered Lists. If none specify "None"')
    publications = forms.CharField(max_length=1000, help_text='Provide the details of your Publications.  Mention Dates. Use Multiple Lines . If multiple Publications use Ordered Lists. If none specify "None"')
    school_studied = forms.CharField(max_length=1000,
        help_text='The Schools you Studied In. With Dates. If Multiple use Ordered Lists')

    work = forms.ModelChoiceField(queryset=University.objects.all() , help_text='Where you work. Company/University name')
    univ_studied =forms.ModelChoiceField(queryset= University.objects.all(), help_text='The University you studied before.')
    work_field_main = forms.ModelChoiceField(queryset= Interest.objects.all() ,
                                             help_text='What are you interested in pursuing as Research Topic/Projects. '
                                                       'Basically why you came to this site.')

    skills = forms.ModelMultipleChoiceField(queryset= Skill.objects.all() , help_text='Your skills.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email_id', 'password',
                  'phone_no', 'bio','image','cv_url','position',
                  'experience','projects_info','publications','school_studied',
                  'work','univ_studied','work_field_main','skills',)
