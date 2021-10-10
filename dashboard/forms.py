from datetime import date
from django import forms
from django.forms import widgets
from .models import assignment, ebook, circular, classes
from users.models import student, teacher
from chat.models import chat_room



class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'



class AssignmentForm(forms.ModelForm):
    class Meta:
        model = assignment
        exclude = ['school', 'subject']
        widgets = {
            'deadline': DateInput()
        }


class BookForm(forms.ModelForm):
    class Meta:
        model = ebook
        exclude = ['school', 'subject']


class CircularForm(forms.ModelForm):
    class Meta:
        model = circular
        exclude = ['school']


class ClassForm(forms.ModelForm):
    class Meta:
        model = classes
        exclude = ['school', 'subject', 'teacher']
        widgets = {
            'date': DateInput(),
            'start': TimeInput(),
            'end': TimeInput()
        }


class ChatRoomForm(forms.ModelForm):
    class Meta:
        model = chat_room
        exclude = ['school', 'teacher']


class StudentForm(forms.ModelForm):
    class Meta:
        model = student
        exclude = ['school']
        widgets = {
            'dob': DateInput()
        }

class TeacherForm(forms.ModelForm):
    class Meta:
        model = teacher
        exclude = ['school']