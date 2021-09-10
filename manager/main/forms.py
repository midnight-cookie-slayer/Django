from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.core.validators import RegexValidator

"""class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'group'}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={'class': 'group'}))
    #username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'group'}))
    #email = forms.CharField(label='Электронная почта', widget=forms.TextInput(attrs={'class': 'group'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        print(cd)
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']"""


class UserRegisterForm(UserCreationForm):

    username = forms.CharField(label='Имя пользователя', help_text='Введите корректное имя пользователя', widget=forms.TextInput(attrs={'class':'form-control'}))

    email = forms.CharField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))

    phone_regex = RegexValidator(regex=r'^\+?1?\d{12,12}$', message="format: '+999999999'. Up to 12 digits allowed.")

    last_name = forms.CharField(validators=[phone_regex], max_length=17, label='Номер телефона', widget=forms.TextInput(attrs={'class': 'form-control'}))

    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    """class Meta:
        model = forms.Userfields = ('username', 'email', 'last_name', 'password1', 'password2')"""

    class Meta:
        model = User
        fields = ('username', 'email', 'last_name', 'password1', 'password2')


"""class LogIn(forms.Form):
    username= forms.CharField(max_length= 25,label="Enter username")
    password= forms.CharField(max_length= 30, label='Password', widget=forms.PasswordInput)"""

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))