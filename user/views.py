from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

def register(request):

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, 'Your account is created '+username)
            return redirect('login')
    else:
        form = CreateUserForm()
    context = {'form':form}
    return render(request, 'user/register.html', context)

def login_user(request):
    next = None
    return_url = request.GET.get('next')
    if request.method == "POST":
      form = AuthenticationForm(request=request, data=request.POST)
      if form.is_valid():
        uname = form.cleaned_data['username']
        upass = form.cleaned_data['password']
        user = authenticate(username=uname, password=upass)
        login(request, user)
        
        messages.success(request, 'Logged in successfully !!')
        request.session['user'] = request.user.id
        if return_url:
                return HttpResponseRedirect(return_url)
        else:
            return_url = None
            return redirect('/mystore')        
        
    else:
        form = AuthenticationForm()
    context = {'form':form}
    return render(request, 'user/login.html',context)
def profile(request):
    return render(request, 'user/profile.html')

def user_logout(request):
    logout(request)
    return redirect('login')
