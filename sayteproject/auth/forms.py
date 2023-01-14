from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def email_validate(value):
      if User.objects.filter(email=value).exists():
        raise forms.ValidationError(
            'Такая почта уже зарегистрирована!',
            params={'value': value},
        )  

class LoginForm(forms.Form):
    #email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Почта'}))
    username = forms.CharField(label='Логин')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))

    class Meta:
        model = User
        labels = {
            'email' : 'Почта',
        }

class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Логин'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Почта'}), validators=[email_validate])
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Еще раз'}))

    class Meta:
        model = User
        fields = ('username', 'email')
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

