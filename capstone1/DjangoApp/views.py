from django.shortcuts import render
from .models import Person


# Create your views here.
# from capstone1.DjangoApp.forms import PolicyForm


def home(request):
    return render(request, "index.html")


def policy(request):
    rule = request.POST.get('rule')
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
