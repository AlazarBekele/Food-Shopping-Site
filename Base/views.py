from django.shortcuts import render
from .models import Index

# Create your views here.

def index (request):
    
    apply = Index.objects.filter().order_by('-Title')[:10]

    context = {
        'apply' : apply
    }

    return render (request, 'index.html', context=context)