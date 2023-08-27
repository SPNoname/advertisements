from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.POST == 'POST':
        form = UserCreationForm()
        if form.is_valid():
            form.save()
    messages.success(request, 'аккаунт успешно создан')
        
    
    else:
        form = UserCreationForm()
    context = {
        'form':form
    }
    return render(request, 'register.html', context)

def my_login(request):
    redirect_url = reverse("profile")
    if request.user.is_authenticated:
        return redirect(redirect_url)
    if request.method == "GET":
        return render(request, 'myauth/login.html')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("main-page")
    return render(request, 'myauth/login.html', {"error": "Пользователь не найден"})


def profile(request):
    return render(request, 'myauth/profile.html')


def my_logout(request):
    redirect_to = reverse("main-page")
    logout(request)
    return redirect(redirect_to)