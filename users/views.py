from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .form import UserForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.decorators import login_required


def userlogin(req):
    if req.user.is_authenticated:
        return redirect('profiles')

    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error('username does not exist')

        user = authenticate(req, username=username, password=password)
        if user != None:
            login(req, user)
            return redirect('all-articles')

    return render(req, 'login.html')


def userRegister(req):
    if req.user.is_authenticated:
        return redirect('all-articles')

    form = UserForm()

    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(req, user)
            return redirect('all-articles')     # redirect to edit
        else:
            messages.error(req, 'User account not valid, try again')

    context = {'form': form}
    return render(req, 'register.html', context)


@login_required(login_url='user-login')
def userLogout(req):
    logout(req)
    return redirect('all-articles')


@login_required(login_url='user-login')
def userEdit(req):
    profile = req.user.profile
    form = ProfileForm(instance=profile)

    if req.method == 'POST':
        form = ProfileForm(req.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('all-articles')

    context = {'form': form}
    return render(req, 'form-user.html', context)


def settings(req, pk):
    userCust = Profile.objects.get(id=pk)
    articles = userCust.article_set.all()
    context = {'articles': articles, 'user': userCust}
    return render(req, 'settings.html', context)
