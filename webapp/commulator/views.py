from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as auth_login
from .forms import SignupForm, LoginForm


# Create your views here.
def base(request):
    return render(request, "base.html")

def signup(request):
    form = SignupForm(request.POST or None)
    if form.is_valid():
        form.save()
        # authenticate the user and redirect to the home page
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        confirm_password = form.cleaned_data['password2']
        user = authenticate(request, username=username, password=password, confirm_password=confirm_password)
        if user is not None:
            auth_login(request, user)
            return redirect('base')
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('base')
        else:
            # Handle invalid login
            pass
    return render(request, 'login.html')

