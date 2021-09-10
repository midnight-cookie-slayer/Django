from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserLoginForm, UserRegisterForm


def index(request):
    """companys = Company.objects.get(id=1)"""
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


"""def log_in(request):
    uservalue = ''
    passwordvalue = ''

    form = LogIn(request.POST or None)
    if form.is_valid():
        uservalue = form.cleaned_data.get("username")
        passwordvalue = form.cleaned_data.get("password")

        user = authenticate(username=uservalue, password=passwordvalue)
        if user is not None:
            login(request, user)
            context = {'form': form, 'error': 'The login has been successful'}

            return render(request, 'main/log_in.html', context)
        else:
            context = {'form': form, 'error': 'The username and password combination is incorrect'}

            return render(request, 'main/log_in.html', context)

    else:
        context = {'form': form}
        return render(request, 'main/log_in.html', context)"""


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            form = UserLoginForm()
    else:
        form = UserLoginForm()
    return render(request, 'main/log_in.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect('home')


"""def registration(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return redirect('home')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'main/registration.html', {'user_form': user_form})"""
"""user = form.save(commit=False)
user.set_password(form.cleaned_data['password'])
user.save()
return redirect('home')"""


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('log_in')
    else:
        form = UserRegisterForm()

    return render(request,'main/registration.html',{'form':form})

