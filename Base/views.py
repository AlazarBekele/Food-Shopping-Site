from django.shortcuts import render, redirect
from .models import Index
from .forms import LoginInput
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages



# Create your views here.

def index (request):
    
    apply = Index.objects.all()
    leatest_news = Index.objects.filter().order_by('-Title')

    context = {
        'apply' : apply,
        'leatest' : leatest_news
    }

    return render (request, 'index.html', context=context)



def login_check (request):

    form = LoginInput (request.POST or None)
    if request.method == 'POST':
        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)

            if user is  None:
                messages.success(request, 'No !!')
            elif user is not None:
                login (request, user)
                messages.success (request, ('Yes!!'))
                return redirect ('index')


    context = {
        'form' : form
    }

    return render (request, 'Login.html', context=context)