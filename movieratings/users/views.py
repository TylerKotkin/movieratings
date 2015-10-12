from django.shortcuts import redirect, render

from django.contrib.auth import authenticate, login, logout

from .forms import UserForm

# Create your views here.


def logout_view(request):
    logout(request)
    messages.add_message(request,
                                 messages.SUCCESS,
                                 "{} succesfully logged out.".format(user.username))
    return redirect('top_movies')


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


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            messages.add_message(request,
                                 messages.SUCCESS,
                                 "Welcome {}!".format(user.username))
            return redirect('top_movies')

        else:
            return render(request,
                          'users/login.html',
                          {'failed': True,
                           'username': username})

    return render(request,
                  'users/login.html',
                  {})