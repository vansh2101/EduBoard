from django.contrib import admin
from .models import assignment, circular, ebook, classes


# Register your models here.

admin.site.register(assignment)
admin.site.register(circular)
admin.site.register(ebook)
admin.site.register(classes)