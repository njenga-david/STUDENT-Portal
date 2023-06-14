from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def loginPage(request):
    user = None  # Initialize the 'user' variable

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)  # Pass the 'user' object, not the username
        return redirect('home')
    else:
        messages.info(request, 'Username or password is incorrect')
        return render(request, 'login.html')

    context = {}
    return render(request, 'login.html')

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')

            messages.success(request, 'Account was created for ' + user)
            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)

def homePage(request):
    return render(request, 'index.html')
