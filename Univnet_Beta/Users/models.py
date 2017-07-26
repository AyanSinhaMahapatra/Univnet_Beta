from django.db import models

class student(models.Model):
    username_roll=models.IntegerField(max_length=15)
    email_id=models.CharField(max_length=30)
    password=models.CharField(max_length=20)
    name=models.CharField(max_length=30)
    phone_no=models.CharField(max_length=15)
    bio=models.CharField(max_length=200)
    image_url=models.CharField(max_length=1000)
    cv_url=models.CharField(max_length=1000)
    year_of_study=models.IntegerField(max_length=1)
    course_name=models.ForeignKey(courses, on_delete=models.CASCADE)

    dept_stud=models.ForeignKey(departments,on_delete=models.CASCADE)
    work_field_main = models.ForeignKey(interests, on_delete=models.CASCADE)
    work_field_sub = models.ForeignKey(interests, on_delete=models.CASCADE)

    def __str__(self):
        return self.username_roll


class alumni(models.Model):
    user_name=models.CharField(max_length=20)  #User Generated Value
    email_id = models.CharField(max_length = 30)
    password = models.CharField(max_length = 20)
    name = models.CharField(max_length = 30)
    phone_no = models.CharField(max_length = 15)
    bio = models.CharField(max_length = 200)
    image_url = models.CharField(max_length = 1000)
    cv_url = models.CharField(max_length = 1000)
    works_at = models.CharField(max_length = 50)  #Company or University, Whatever


    dept_alum = models.ForeignKey(departments, on_delete = models.CASCADE)
    work_field_main = models.ForeignKey(interests, on_delete = models.CASCADE)
    work_field_sub = models.ForeignKey(interests, on_delete = models.CASCADE)

    def __str__(self):
        return self.user_name

#Basically What they work on/ want to work/want to find collaborations on
class interests(models.Model):
    interest_name = models.CharField(max_length = 30)

    def __str__(self):
        return self.interest_name

 # Their Department Of Study
class departments(models.Model):
    dept_name = models.CharField(max_length = 30)

    def __str__(self):
        return self.dept_name

# Like B.E. or B.Tech or M.Tech
class courses(models.Model):
    course_name = models.CharField(max_length=10)

    def __str__(self):
        return self.course_name
