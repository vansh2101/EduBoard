#import standard libraries
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages

#import my code
from .forms import LoginForm, RegisterForm
from .models import accounts, school, teacher, student



# Create your views here.

def login(request):
    if request.method == 'POST':
        #if POST request is sent by the user
        form = LoginForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            user = auth.authenticate(username=data['email'], password=data['password'])

            if user is not None:
                auth.login(request, user)
                return redirect('/dashboard/')

            else:
                messages.error(request, 'Invalid Credentials')
                return redirect('/auth/login/')

        else:
            return redirect('/auth/login/')

    else:
        #if GET request is sent by the user
        form = LoginForm()
        return render(request, 'login.html', {'form': form})



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['school_email']).exists():
                messages.error(request, 'Entered email is already registered')
                return redirect('/auth/register')

            data = form.cleaned_data

            #user saved for authentication
            user = User.objects.create_user(username=data['school_email'], first_name=data['school_name'], email=data['school_email'], password=data['password'])
            user.save()

            #user saved into account database
            acc = accounts.objects.create(user=user, type='school')
            acc.save()

            #user saved into school database
            sch = school.objects.create(name=data['school_name'], email=data['school_email'], phone_no=data['school_phone_number'], address=data['school_address'], city=data['city'], country=data['country'], plan='standard')
            sch.save()

            return redirect('/auth/login')

        else:
            if 'school_phone_number' in str(form.errors):
                messages.error(request, 'Please type in a valid 10 digit phone number')

            elif "Passwords don&#x27;t match" in str(form.errors):
                messages.error(request, 'Passwords don\'t match')

            else:
                messages.error(request, 'Sorry!! Something went wrong')
            
            return redirect('/auth/register')

    else:
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})


def logout(request):
    auth.logout(request)
    return redirect('/')