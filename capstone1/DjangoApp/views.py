from django.shortcuts import render, redirect
from .models import Processed, User, UserManager, set_name
from .forms import SignUpForm, LoginForm
from .controller import Controller
from .ui import ConsoleUI
from django.contrib.auth.models import User

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
    output = User.objects.all()
    return render(request, "dis_user.html", {'output': output})


def create_user(request):
    if request.method == 'POST':
        new_user = UserManager.create_user(request.POST.get('user'), request.POST.get('password'))
        new_user.fullname = request.POST.get('fullname')
        new_user.save()
    return render(request, "create_user.html")


def mod_user(request):
    return render(request, "mod_user.html")


def del_user(request):
    if request.method == 'POST':
        query = User.objects.get(username=request.POST.get('user'))
        query.delete()
    return render(request, "del_user.html")


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        user_info = UserManager.create_user(UserManager(), request.POST.get('username'), request.POST.get('password'))

        set_name(user_info, request.POST.get('first_name'), request.POST.get('last_name'))
        user_info.save()

        if form.is_valid():
            form.save()

        return redirect("/home")
    else:
        form = SignUpForm
    return render(request, "signup.html", {"form": form})


def login(request):
    user_value = ''
    password_value = ''

    form = LoginForm(request.POST or None)
    if form.is_valid():
        user_value = form.cleaned_data.get("username")
        password_value = form.cleaned_data.get("password")
        print(user_value)
        print(password_value)

        if User.objects.filter(username=user_value).exists():
            print("I got into the if statement")
            the_user = User.objects.get(username=user_value)
            if the_user.check_password(password_value):
                context = {'form': form, 'error': 'The login has been successful'}
                return render(request, 'index.html', context)
            else:
                context = {'form': form, 'error': 'The username and password combination is incorrect'}
                return render(request, 'login.html', context)
        else:
            print("Could not find user")
    else:
        context = {'form': form}
        return render(request, 'login.html', context)

