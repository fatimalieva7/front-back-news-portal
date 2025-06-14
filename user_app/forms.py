from django import forms
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class NewsForm(forms.ModelForm):
    def clean(self):
        if not self.instance.author and not self.initial.get('author'):
            raise ValidationError("Только авторизованные пользователи могут создавать новости")
        return super().clean()



class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
            'email': forms.EmailInput(attrs={'type': 'email'}),
            'username': forms.TextInput(attrs={'type': 'text'}),
        }


class UserLoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите имя пользователя',
            'autofocus': True
        }),
        label='Имя пользователя'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите пароль'
        }),
        label='Пароль'
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError("Неверное имя пользователя или пароль")
            if not user.is_active:
                raise forms.ValidationError("Аккаунт отключен")
        return cleaned_data