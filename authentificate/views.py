from django.shortcuts import render, render_to_response, HttpResponseRedirect
from django.http import Http404
from django.contrib import auth
from django.contrib.auth.models import User
# Create your views here.

def login(request):
    if request.method =='POST':
        username = request.POST.get('login')
        passdw = request.POST.get('passwd')
        user = auth.authenticate(username=username, password=passdw)
        if user:
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'login.html', {'username': username, 'errors': True})
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

