from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


from .forms import UserForm
# Create your views here.


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            return redirect('top_movies')

        else:
            return render(request,
                          'users/login.html',
                          {'failed': True,
                           'username': username})

    return render(request,
                  'users/login.html',
                  {})


def user_register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            user = form.save()
            password = user.password

            user.set_password(password)
            user.save()

            user = authenticate(username=user.username, password=password)

            login(request, user)
            return redirect('top_movies')
    else:
        form = UserForm()
    return render(request, 'users/register.html',
                  {'form': form})



def logout_view(request):
    logout(request)
    return redirect('top_movies')
