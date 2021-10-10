from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class accounts(models.Model):
    type_choices = [('student', 'student'), ('teacher', 'teacher'), ('school', 'school')]

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    type = models.CharField(choices=type_choices, max_length=7)

    def __str__(self):
        return "{}".format(self.user.username)


class school(models.Model):
    plan_choice = [('standard', 'standard'), ('hacker', 'hacker'), ('premium', 'premium')]

    name = models.CharField(max_length=200)
    email = models.CharField(max_length=150, primary_key=True)
    phone_no = models.CharField(max_length=10)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    plan = models.CharField(choices=plan_choice, max_length=8, default='standard')

    def __str__(self):
        return "{}".format(self.name)


class teacher(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=150, primary_key=True)
    phone_no = models.CharField(max_length=10)
    subject = models.CharField(max_length=100)
    school = models.ForeignKey(school, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.name, self.school.name)


class student(models.Model):
    adm_no = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=150, primary_key=True)
    phone_no = models.CharField(max_length=10)
    dob = models.DateField()
    grade = models.IntegerField()
    section = models.CharField(max_length=100)
    school = models.ForeignKey(school, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.name, self.school.name)