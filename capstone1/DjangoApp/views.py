from django.shortcuts import render, redirect
from .models import Person
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from .controller import Controller
from .ui import ConsoleUI

# Create your views here.
# from capstone1.DjangoApp.forms import PolicyForm

con = Controller()
ui = ConsoleUI()


def home(request):
    return render(request, "index.html")


def policy(request):
    rule = request.POST.get('rule')
    con.process_input(rule)
    return render(request, "policy.html")


def analysis(request):
    return render(request, "analysis.html")


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
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            raw_password = form.cleaned_data.get('password1')

            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def login(request):
    uservalue = ""
    passwordvalue = ""
    form = LoginForm(request.POST or None)
    if form.is_valid():
        uservalue = form.cleaned_data.get("username")
        passwordvalue = form.cleaned_data.get("password")

        user = authenticate