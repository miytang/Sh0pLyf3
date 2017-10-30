from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from loginpage.forms import SignUpForm


def home(request):
    return render(request, 'loginpage/base.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('start')
    else:
        form = SignUpForm()
    return render(request, 'loginpage/signup.html', {'form': form})
