from django.contrib import admin
from .models import accounts, school, teacher, student


# Register your models here.

admin.site.register(accounts)
admin.site.register(school)
admin.site.register(teacher)
admin.site.register(student)