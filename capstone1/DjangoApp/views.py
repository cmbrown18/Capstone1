from django.shortcuts import render, redirect
from .models import Processed, User
from .forms import SignUpForm, LoginForm
from .controller import Controller
from .ui import ConsoleUI
from django.contrib.auth.models import User, UserManager

# Create your views here.
# from capstone1.DjangoApp.forms import PolicyForm

con = Controller()
ui = ConsoleUI()


def home(request):
    """
    Returns the home page
    """
    return render(request, "index.html")


def policy(request):
    """
    Policy accepts a natural sentence and sends it to the NLP
    """
    if request.method == 'POST':
        Processed.objects.all().delete()
        rule = request.POST.get('rule')
        con.process_input(rule)
    return render(request, "policy.html")


def analysis(request):
    """
    Returns the analysis page
    """
    return render(request, "analysis.html")


def processed(request):
    """
    Returns all the processed data along with the site for processed data
    """
    result = Processed.objects.all()
    return render(request, "processed.html", {'result': result})


def user(request):
    """
    Returns the user menu
    """
    return render(request, "user.html")


def display_user(request):
    """
    Displays a well formatted version of all the current users
        that are signed up with this project
    """
    output = User.objects.all()
    return render(request, "dis_user.html", {'output': output})


def create_user(request):
    """
    TODO: We need to talk about if this can be deleted or not I think it can be because we can create users in the signup
        and have no real reason to create them any other way.

    Creates a user from the user menu and saves it to the models database
    """
    if request.method == 'POST':
        new_user = UserManager.create_user(request.POST.get('user'), request.POST.get('password'))
        new_user.fullname = request.POST.get('fullname')
        new_user.save()
    return render(request, "create_user.html")


def mod_user(request):
    """
    TODO: We need to actually set this up if we wanna use it to modify users. If we do this we will need to remember
        to modify their user policy file's name as well. Might be a little annoying but functional to use later and would
        be cool to show that this works.

    Modifies the user in the database and changes everything that regards to said user
    """
    return render(request, "mod_user.html")


def del_user(request):
    """
    Deletes the user based off the username

    TODO: Might not be a bad idea here to check if they have a policy file and delete that as well. Food for Thought
    """
    if request.method == 'POST':
        query = User.objects.get(username=request.POST.get('user'))
        query.delete()
    return render(request, "del_user.html")


def signup(request):
    """
    Returns the signup pages, creates a user with all of the fields filled in.
    """

    if request.method == 'POST':
        form = SignUpForm(request.POST)

        user_info = User()

        user_info.username = request.POST.get('username')
        user_info.set_password(request.POST.get('password2'))
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
    """
    Returns the login form and checks if the user exists then checks the password to make sure it is right,
        if it is right then it returns to the menu page.
    """

    user_value = ''
    password_value = ''

    form = LoginForm(request.POST or None)
    if form.is_valid():
        user_value = form.cleaned_data.get("username")
        password_value = form.cleaned_data.get("password")

        if User.objects.filter(username=user_value).exists():
            the_user = User.objects.get(username=user_value)

            if the_user.check_password(raw_password=password_value):
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

# def user_request(request):
