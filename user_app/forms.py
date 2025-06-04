from django import forms
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

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
class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
            'username': forms.TextInput(attrs={'type': 'text'}),
        }

class UserSignForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]

