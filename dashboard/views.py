from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from datetime import datetime
from background_task import background

from .models import assignment, circular, ebook, classes
from .forms import AssignmentForm, BookForm, CircularForm, ClassForm, ChatRoomForm, StudentForm, TeacherForm
from users.models import accounts, school, student, teacher
from chat.models import chat_room



# Create your views here.

@login_required(login_url='/auth/login/', redirect_field_name='/dashboard')
def dashboard(request):
    type = accounts.objects.get(user=request.user).type

    if type == 'school':
        user = school.objects.get(email=request.user.username)
        students = student.objects.filter(school=user)[::-1][:3]
        teachers = teacher.objects.filter(school=user)[::-1][:3]
        meet = classes.objects.filter(school=user)[::-1][:3]

        keys = {
            'user': user,
            'type':type,
            'students': students,
            'teachers': teachers,
            'classes': meet,
        }

        return render(request, 'school_dashboard.html', keys)

    elif type == 'teacher':
        user = teacher.objects.get(email=request.user.username)
        assign = assignment.objects.filter(subject=user.subject, school=user.school)[::-1]
        circulars = circular.objects.filter(school=user.school, circular_for='teacher')[::-1]
        books = ebook.objects.filter(school=user.school, subject=user.subject)[::-1]
        meet = classes.objects.filter(school=user.school, teacher=user)[::-1]

        keys = {
            'user': user, 
            'assignment':assign[:3], 
            'circular': circulars[:3], 
            'books': books[:3], 
            'classes': meet[:3],
            'time': datetime.now(),
            'type': type
        }

        return render(request, 'dashboard.html', keys)

    elif type == 'student':
        user = student.objects.get(email=request.user.username)
        assign = assignment.objects.filter(grade=user.grade, section=user.section, school=user.school)[::-1]
        circulars = circular.objects.filter(grade=user.grade, school=user.school, circular_for='student')[::-1]
        books = ebook.objects.filter(school=user.school, grade=user.grade)[::-1]
        meet = classes.objects.filter(school=user.school, grade=user.grade, section=user.section)[::-1]

        keys = {
            'user': user, 
            'assignment':assign[:3], 
            'circular': circulars[:3], 
            'books': books[:3], 
            'classes': meet[:3],
            'time': datetime.now(),
            'type': type
        }

        return render(request, 'dashboard.html', keys)


@login_required(login_url='/auth/login/', redirect_field_name='/dashboard/classes')
def meets(request):
    type = accounts.objects.get(user=request.user).type
    if type == 'student':
        user = student.objects.get(email=request.user.username)
        meet = classes.objects.filter(school=user.school, grade=user.grade, section=user.section)[::-1]

    elif type == 'teacher':
        user = teacher.objects.get(email=request.user.username)
        meet = classes.objects.filter(school=user.school, teacher=user)[::-1]

    elif type == 'school':
        user = school.objects.get(email=request.user.username)
        meet = classes.objects.filter(school=user)[::-1]

    return render(request, 'classes.html', {'meets':meet, 'type': type, 'time': datetime.now(),})


@login_required(login_url='/auth/login/', redirect_field_name='/dashboard/assignments')
def assignments(request):
    type = accounts.objects.get(user=request.user).type
    if type == 'student':
        user = student.objects.get(email=request.user.username)
        assign = assignment.objects.filter(grade=user.grade, section=user.section, school=user.school)[::-1]

    else:
        user = teacher.objects.get(email=request.user.username)
        assign = assignment.objects.filter(subject=user.subject, school=user.school)[::-1]

    return render(request, 'assignments.html', {'assignments':assign, 'type':type})


@login_required(login_url='/auth/login/', redirect_field_name='/dashboard/circulars')
def circulars(request):
    type = accounts.objects.get(user=request.user).type
    if type == 'student':
        user = student.objects.get(email=request.user.username)
        circulars = circular.objects.filter(grade=user.grade, school=user.school, circular_for='student')[::-1]
    elif type == 'teacher':
        user = teacher.objects.get(email=request.user.username)
        circulars = circular.objects.filter(circular_for='teacher', school=user.school)[::-1]

    elif type == 'school':
        user = school.objects.get(email=request.user.username)
        circulars = circular.objects.filter(school=user)[::-1]
    
    return render(request, 'circulars.html', {'circulars':circulars, 'type':type})


@login_required(login_url='/auth/login/', redirect_field_name='/dashboard/ebooks')
def ebooks(request):
    type = accounts.objects.get(user=request.user).type
    if type == 'student':
        user = student.objects.get(email=request.user.username)
        books = ebook.objects.filter(school=user.school, grade=user.grade)
    else:
        user = teacher.objects.get(email=request.user.username)
        books = ebook.objects.filter(school=user.school, subject=user.subject)
    
    return render(request, 'ebooks.html', {'books':books, 'type':type})


@login_required(login_url='/auth/login/', redirect_field_name='/dashboard/')
def forms(request, task):
    type = accounts.objects.get(user=request.user).type

    if request.method == 'POST':
        if type == 'teacher':
            user = teacher.objects.get(email=request.user.username)
        elif type == 'school':
            user = school.objects.get(email=request.user.username)
        else:
            return redirect('/dashboard/')

        if task == 'assignments':
            form = AssignmentForm(request.POST)

            if form.is_valid():
                data = form.cleaned_data
                asm = assignment.objects.create(
                    topic=data['topic'],
                    subject=user.subject,
                    deadline=data['deadline'],
                    description=data['description'],
                    grade=data['grade'],
                    section=data['section'],
                    school=user.school
                )
                asm.save()

                return redirect('/dashboard/assignments')

            else:
                return redirect('/dashboard/add/assignments')

        elif task == 'circular':
            form = CircularForm(request.POST)

            if form.is_valid():
                data = form.cleaned_data
                cir = circular.objects.create(
                    topic=data['topic'],
                    description=data['description'],
                    grade=data['grade'],
                    circular_for=data['circular_for'],
                    school=user
                )
                cir.save()

                return redirect('/dashboard/circulars')

            else:
                return redirect('/dashboard/add/circular')

        elif task == 'ebook':
            form = BookForm(request.POST, request.FILES)

            if form.is_valid():
                data = form.cleaned_data
                book = ebook.objects.create(
                    name=data['name'],
                    subject=user.subject,
                    file=data['file'],
                    grade=data['grade'],
                    school=user.school
                )
                book.save()

                return redirect('/dashboard/ebooks')

            else:
                return redirect('/dashboard/add/ebook')

        elif task == 'class':
            form = ClassForm(request.POST)

            if form.is_valid():
                data = form.cleaned_data
                clas = classes.objects.create(
                    topic=data['topic'],
                    subject=user.subject,
                    date=data['date'],
                    start=data['start'],
                    end=data['end'],
                    url=data['url'],
                    grade=data['grade'],
                    section=data['section'],
                    teacher=user,
                    school=user.school
                )
                clas.save()

                return redirect('/dashboard/classes')

            else:
                return redirect('/dashboard/add/class')

        elif task == 'chat group':
            form = ChatRoomForm(request.POST)

            if form.is_valid():
                data = form.cleaned_data

                room = chat_room.objects.create(
                    name=data['name'],
                    grade=data['grade'],
                    section=data['section'],
                    teacher=user,
                    school=user.school
                )
                room.save()

                return redirect('/chat')

        elif task == 'student':
            form = StudentForm(request.POST)

            if form.is_valid():
                data = form.cleaned_data

                stud = student.objects.create(
                    adm_no=data['adm_no'],
                    name=data['name'],
                    email=data['email'],
                    phone_no=data['phone_no'],
                    dob=data['dob'],
                    grade=data['grade'],
                    section=data['section'],
                    school=user
                )
                stud.save()

                #user saved for authentication
                user = User.objects.create_user(
                    username=data['email'], 
                    first_name=data['name'], 
                    email=data['email'], 
                    password=data['phone_no']
                    )
                user.save()

                #user saved into account database
                acc = accounts.objects.create(user=user, type='student')
                acc.save()

                return redirect('/dashboard/students')

        elif task == 'teacher':
            form = TeacherForm(request.POST)

            if form.is_valid():
                data = form.cleaned_data

                teach = teacher.objects.create(
                    name=data['name'],
                    email=data['email'],
                    phone_no=data['phone_no'],
                    subject=data['subject'],
                    school=user
                )
                teach.save()

                #user saved for authentication
                user = User.objects.create_user(
                    username=data['email'], 
                    first_name=data['name'], 
                    email=data['email'], 
                    password=data['phone_no']
                    )
                user.save()

                #user saved into account database
                acc = accounts.objects.create(user=user, type='teacher')
                acc.save()

                return redirect('/dashboard/teachers')

    else:
        if task == 'assignments':
            form = AssignmentForm()

        elif task == 'circular':
            form = CircularForm()

        elif task == 'ebook':
            form = BookForm()

        elif task == 'class':
            form = ClassForm()

        elif task == 'chat group':
            form = ChatRoomForm()

        elif task == 'student':
            form = StudentForm()

        elif task == 'teacher':
            form = TeacherForm()

        else:
            return redirect('/dashboard/')

        keys = {
            'title': task.capitalize(),
            'form': form,
            'type': type
        }
        return render(request, 'forms.html', keys)


@login_required(login_url='/auth/login/', redirect_field_name='/dashboard/students')
def students(request):
    type = accounts.objects.get(user=request.user).type
    user = school.objects.get(email=request.user.username)
    stud = student.objects.filter(school=user)

    keys = {
        'type': type,
        'page': 'students',
        'users': stud
    }
    return render(request, 'user_list.html', keys)


@login_required(login_url='/auth/login/', redirect_field_name='/dashboard/teachers')
def teachers(request):
    type = accounts.objects.get(user=request.user).type
    user = school.objects.get(email=request.user.username)
    teach = teacher.objects.filter(school=user)

    keys = {
        'type': type,
        'page': 'teachers',
        'users': teach
    }
    return render(request, 'user_list.html', keys)




'''Background Functions'''

@background(schedule=5)
def del_class():
    clas = classes.objects.all()

    for i in clas:
        if i.date < datetime.now().date() or (i.end < datetime.now().time() and i.date <= datetime.now().date()):
            obj = classes.objects.get(id=i.id)
            obj.delete()

del_class(repeat=3600, repeat_until=None)