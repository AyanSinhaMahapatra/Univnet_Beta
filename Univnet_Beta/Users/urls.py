from django.conf.urls import url
from . import views

app_name='Users'

urlpatterns = [
    #/user_home/

    #/user_home/user/<username_roll>/
    url(r'^(?P<username_roll_request>[0-9]+)/$', views.details_stud , name='details_stud'),

    #/user_home/alumni/<username>/
    url(r'^(?P<username_roll_request>[0-9]+)/$', views.details_alumni, name='details_alumni'),

]