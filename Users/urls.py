from django.conf.urls import url
from . import views

app_name = 'Users'

urlpatterns = [
    # /

    # home_page for Students
    # /student/<username_roll>/
    url(r'^student/(?P<username_roll_request>[0-9]+)/$', views.details_stud, name='details_stud'),

    # home_page for Alumni
    # /alumni/<username>/
    url(r'^alumni/(?P<username_roll_request>[a-z]+[0-9]+)/$', views.details_alumni, name='details_alumni'),

]
