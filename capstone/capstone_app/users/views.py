from django.shortcuts import render
from django.contrib.auth import authenticate, login as django_login 
from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.

def login(request):
    template = "login_screen.html"
    content = {}
    if request.method == 'POST':
        user_name = request.POST.get('inputUserName')
        password = request.POST.get('inputPassword')
        user = authenticate(request, username=user_name, password=password)

        if user is not None:
            django_login(request, user)
            response_request = request.GET.get('next', None)
            if not response_request: 
                response_request = '/'
            return HttpResponseRedirect(response_request)
        else:
            messages.warning(request,'Not a vaild user name. Please check your credentials and try again!',extra_tags='no_user')
    else:
        messages.warning(request,'Please sign in to access all features of our website!',extra_tags='no_user')

    return render(request, template, content)