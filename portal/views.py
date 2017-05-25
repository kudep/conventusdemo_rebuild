from django.shortcuts import render, redirect
from django.contrib import auth

# Create your views here.


def portal(request):
    if not auth.get_user(request).is_authenticated():
        return redirect('/')
    print('Run story script')
    args = dict()
    args['username'] = auth.get_user(request).username
    print(args['username'])
    return render(request, 'portal/portal.html', args)


def sys_login(request):
    args = dict()
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        print("auth")
        if user is not None:
            auth.login(request, user)
            args['username'] = auth.get_user(request).username
            return render(request, 'portal/portal.html', args)
        else:
            args['login_error'] = "Пользователь не найден"
            print("Error")
            return render(request, 'portal/sys_login.html', args)

    else:
        return render(request, 'portal/sys_login.html', args)


def sys_logout(request):
    args = dict()
    auth.logout(request)
    return render(request, 'home/home.html', args)

