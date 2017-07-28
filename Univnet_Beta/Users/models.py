from django.db import models


# Like B.E. or B.Tech or M.Tech
class Course(models.Model):
    course_name = models.CharField(max_length=100)

    def __str__(self):
        return self.course_name


# Basically What they work on/ want to work/want to find collaborations on
class Interest(models.Model):
    interest_name = models.CharField(max_length=100)

    def __str__(self):
        return self.interest_name

        # Their Department Of Study


class Level(models.Model):
    dept_name = models.CharField(max_length=100)

    def __str__(self):
        return self.dept_name


class Student(models.Model):
    username_roll = models.IntegerField(primary_key=True)
    email_id = models.EmailField()
    password = models.CharField(max_length=40)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_no = models.IntegerField()
    bio = models.TextField()
    image = models.FileField()
    cv_url = models.CharField(max_length=300)
    year_of_study = models.IntegerField()
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE)

    dept_stud = models.ForeignKey(Level, on_delete=models.CASCADE)
    work_field_main = models.ForeignKey(Interest, on_delete=models.CASCADE)

    def __str__(self):
        return f"Roll No: {self.username_roll}"


class Alumni(models.Model):
    user_name = models.CharField(primary_key=True, max_length=20)  # User Generated Value, alpha-numeric
    email_id = models.EmailField()
    password = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_no = models.IntegerField()
    bio = models.TextField()
    image = models.FileField()
    cv_url = models.CharField(max_length=300)
    works_at = models.CharField(max_length=50)  # Company or University, Whatever

    dept_alum = models.ForeignKey(Level, on_delete=models.CASCADE)
    work_field_main = models.ForeignKey(Interest, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_name
