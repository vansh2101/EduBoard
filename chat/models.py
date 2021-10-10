from users.models import school, teacher
from django.db import models



# Create your models here.

class chat_room(models.Model):
    name = models.CharField(max_length=100)
    grade = models.IntegerField()
    section = models.CharField(max_length=100)
    teacher = models.ForeignKey(teacher, on_delete=models.CASCADE)
    school = models.ForeignKey(school, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.name, self.school.name)