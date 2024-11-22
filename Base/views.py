from django.shortcuts import render
from .models import Index

# Create your views here.

def index (request):
    
    apply = Index.objects.all()

    context = {
        'apply' : apply
    }

    return render (request, 'index.html', context=context)