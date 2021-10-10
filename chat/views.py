from dashboard.models import classes
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import chat_room
from users.models import accounts,student,teacher,school


# Create your views here.

@login_required(login_url='/auth/login/', redirect_field_name='/chat')
def chat(request):
    type = accounts.objects.get(user=request.user).type

    if type == 'student':
        user = student.objects.get(email=request.user.username)
        room = chat_room.objects.filter(grade=user.grade, section=user.section, school=user.school)

    elif type == 'teacher':
        user = teacher.objects.get(email=request.user.username)
        room = chat_room.objects.filter(teacher=user, school=user.school)

    elif type == 'school':
        user = school.objects.get(email=request.user.username)
        room = chat_room.objects.filter(school=user)

    keys = {
        'type': type,
        'rooms': room,
        'user': user.name
    }

    return render(request, 'chat.html', keys)