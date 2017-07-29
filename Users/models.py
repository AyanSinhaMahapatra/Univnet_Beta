from django.db import models

class Skill(models.Model):
    skill_name=models.CharField(max_length=150)

    def __str__(self):
        return self.skill_name

class School(models.Model):
    school_name=models.CharField(max_length=300)
    def __str__(self):
        return self.school_name

class University(models.Model):
    univ_name=models.CharField(max_length=300)

    def __str__(self):
        return self.univ_name


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


class Level(models.Model):
    dept_name = models.CharField(max_length=100)

    def __str__(self):
        return self.dept_name


class Student(models.Model):
    username_roll = models.CharField(primary_key=True, max_length=12)
    email_id = models.EmailField()

    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=100)
    bio = models.TextField(max_length=1000)
    extra_curr = models.TextField()
    image = models.FileField()
    cv_url = models.CharField(max_length=300)
    year_of_study = models.IntegerField()
    address = models.TextField(default='I live in Kolkata')

    # Important TextFields

    experience = models.TextField()
    projects_info = models.TextField()
    publications = models.TextField()

    # Foreign Key Containers
    school_studied = models.ForeignKey(School, blank=True, on_delete=models.CASCADE)
    univ_studying = models.ForeignKey(University, blank=True, on_delete=models.CASCADE)

    course_name = models.ForeignKey(Course, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    work_field_main = models.ForeignKey(Interest, on_delete=models.CASCADE)

    # Many to Many Fields
    skills = models.ManyToManyField(Skill, blank=True)

    def __str__(self):
        return f"Roll No: {self.username_roll}"


class Alumni(models.Model):
    user_name = models.CharField(primary_key=True, max_length=20)  # User Generated Value, alpha-numeric
    email_id = models.EmailField()
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=100)
    bio = models.TextField(max_length=1000)
    image = models.FileField()
    cv_url = models.CharField(max_length=300)
    position = models.CharField(max_length=50)  # Company or University, Whatever

    # Important TextFields
    experience = models.TextField()
    projects_info = models.TextField()
    publications = models.TextField()

    # Foreign Key Containers
    work = models.ForeignKey(University, on_delete=models.CASCADE)
    work_field_main = models.ForeignKey(Interest, on_delete=models.CASCADE)
    school_studied = models.ForeignKey(School, on_delete=models.CASCADE)
    univ_studied = models.ForeignKey(University,  related_name='%(class)s_requests_created')

    # Many to Many Fields
    skills = models.ManyToManyField(Skill, blank=True)

    def __str__(self):
        return self.user_name
