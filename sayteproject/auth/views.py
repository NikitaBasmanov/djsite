from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth import authenticate, login, get_user_model
from profession.views import index



# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = (cd['username'])
            user = authenticate(request, username=username, password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect(index)
            else:
                form.add_error(None, 'Неправильный логин или пароль')

    else:
        form = LoginForm()
    return render(request, 'auth/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            login(request, new_user)
            return redirect(index)
    else:
        user_form = UserRegistrationForm()
    return render(request, 'auth/register.html', {'form': user_form})