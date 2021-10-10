from django.db import models
from users.models import school, teacher


# Create your models here.

class assignment(models.Model):
    topic = models.CharField(max_length=200)
    subject = models.CharField(max_length=100)
    deadline = models.DateField()
    description = models.CharField(max_length=10000)
    grade = models.IntegerField()
    section = models.CharField(max_length=100)
    school = models.ForeignKey(school, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.topic, self.school.name)


class circular(models.Model):
    for_options = [('student', 'student'), ('teacher', 'teacher')]
    topic = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)
    description = models.CharField(max_length=10000)
    grade = models.IntegerField(default=0)
    circular_for = models.CharField(choices=for_options, max_length=7)
    school = models.ForeignKey(school, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.topic, self.school.name)


class ebook(models.Model):
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=100)
    file = models.FileField(upload_to='ebooks')
    grade = models.IntegerField()
    school = models.ForeignKey(school, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.name, self.school.name)


class classes(models.Model):
    topic = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    date = models.DateField()
    start = models.TimeField()
    end = models.TimeField()
    url = models.URLField()
    grade = models.IntegerField()
    section = models.CharField(max_length=100)
    teacher = models.ForeignKey(teacher, on_delete=models.CASCADE)
    school = models.ForeignKey(school, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.subject, self.school.name)