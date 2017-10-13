from django.shortcuts import render
from website_crawler.authentication.forms import SignupForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if not form.is_valid():
            return render(request, 'authentication/signup.html', {'form': form })
        else:
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            User.objects.create_user(username=username, password=password, email=email)
            user = authenticate(username=username, password=password)
            login(request, user)
            # welcome_post = '{0} has successfully signed up'.format(user.username)
            return redirect('/')
    else:
        return render(request, 'authentication/signup.html', {'form': SignupForm })