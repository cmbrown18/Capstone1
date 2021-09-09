from django.shortcuts import render, redirect
from .models import Person, Processed, Profile
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from .controller import Controller
from .ui import ConsoleUI
from django.contrib.auth.models import User
from passlib.hash import pbkdf2_sha256

# Create your views here.
# from capstone1.DjangoApp.forms import PolicyForm

con = Controller()
ui = ConsoleUI()


def home(request):
    return render(request, "index.html")


def policy(request):
    if request.method == 'POST':
        Processed.objects.all().delete()
        rule = request.POST.get('rule')
        con.process_input(rule)
    return render(request, "policy.html")


def analysis(request):
    return render(request, "analysis.html")


def processed(request):
    result = Processed.objects.all()
    return render(request, "processed.html", {'result': result})


def user(request):
    return render(request, "user.html")


def display_user(request):
    output = Person.objects.all()
    return render(request, "dis_user.html", {'output': output})


def create_user(request):
    if request.method == 'POST':
        new_user = Person()
        new_user.username = request.POST.get('user')
        new_user.fullname = request.POST.get('fullname')
        new_user.password = request.POST.get('password')
        new_user.save()
    return render(request, "create_user.html")


def mod_user(request):
    return render(request, "mod_user.html")


def del_user(request):
    if request.method == 'POST':
        query = Person.objects.get(username=request.POST.get('user'))
        query.delete()
    return render(request, "del_user.html")


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        user_info = Person()
        user_info.username = request.POST.get('username')

        password = pbkdf2_sha256.hash(request.POST.get('password'))
        user_info.password = password
        user_info.first_name = request.POST.get('first_name')
        user_info.last_name = request.POST.get('last_name')
        user_info.save()

        if form.is_valid():
            form.save()

        return redirect("/home")
    else:
        form = SignUpForm
    return render(request, "signup.html", {"form": form})


def login(request):
    uservalue = ''
    passwordvalue = ''

    form = LoginForm(request.POST or None)
    if form.is_valid():
        user_value = form.cleaned_data.get("username")
        passwordvalue = form.cleaned_data.get("password")
        print(user_value)
        print(passwordvalue)

        if Person.objects.filter(username=user_value).exists():
            print("I got into the if statement")
            person = Person.get_Person
            if pbkdf2_sha256.verify(passwordvalue, person.password):
                context = {'form': form, 'error': 'The login has been successful'}
                return render(request, 'login.html', context)
        else:
            context = {'form': form,
                       'error': 'The username and password combination is incorrect'}

            return render(request, 'login.html', context)

    else:
        context = {'form': form}
        return render(request, 'login.html', context)
