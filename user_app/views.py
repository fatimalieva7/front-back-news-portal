from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from pyexpat.errors import messages
from django.contrib import messages
from .forms import UserRegisterForm
from django.shortcuts import render, redirect
from .forms import UserLoginForm

app_name = 'user_app'


def register_user_view(request):
    if request.method == 'POST':
        form_register_user = UserRegisterForm(request.POST)
        if form_register_user.is_valid():
            username = form_register_user.cleaned_data['username']
            email = form_register_user.cleaned_data['email']
            password = form_register_user.cleaned_data['password']

            if User.objects.filter(username=username).exists():
                form_register_user.add_error('username', 'Пользователь с таким именем уже существует.')

            elif User.objects.filter(email=email).exists():
                form_register_user.add_error('email', 'Пользователь с таким email уже существует.')

            else:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                )
                user.save()
                authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('main:index')

    else:
        form_register_user = UserRegisterForm()

    context = {'form_register_user': form_register_user}
    return render(request, 'user_app/register.html', context)


def logout_user_view(request):
    logout(request)
    return redirect('main:index')


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Вы успешно вошли в систему")
                return redirect('main:index')  # Замените на ваш URL
    else:
        form = UserLoginForm()

    return render(request, 'user_app/login.html', {'form': form})
