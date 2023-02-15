from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    return render(request, "inicio/index.html")

@login_required
def things(request):
    return render(request, 'inicio/things.html')

def logout(request):
    logout(request)
    return redirect('index')

def register(request):
    print("paso1")
    data = {
        'form': CustomUserCreationForm()
    }
    print("paso2")
    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)
        print("paso3")
        if form.is_valid():
            print("paso4")
            form.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('index')
        else:
            print("error en is_valid")
            print(form.errors)
            print(form.errors.as_data())
    else:
        print("error en metodo POST")
    return render(request, 'registration/register.html', data)