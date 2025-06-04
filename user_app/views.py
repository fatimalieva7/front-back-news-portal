from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms  import UserRegisterForm, UserSignForm
from django.contrib.auth.decorators import login_required


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


def user_sign_view(request):
    if request.method == 'POST':
        user_sign_form = UserSignForm(request.POST)
        if user_sign_form.is_valid():
            username = user_sign_form.cleaned_data['username']
            password = user_sign_form.cleaned_data['password']

            user = User.objects.get(
                username=username,
                password=password,
            )
            if user is None:
                user_sign_form.add_error('username', 'Пользователь не найден.')
            login(request, user)
            return redirect('main:index')

    else:
        user_sign_form = UserSignForm()

    context = {
        'user_sign_form': user_sign_form
    }
    return render(request, 'user_app/login.html', context)

@login_required
def logout_user_view(request):
    logout(request)
    return redirect('main:index')