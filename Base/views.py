from django.shortcuts import render
from .models import Index

# Create your views here.

def index (request):
    
    apply = Index.objects.all()
    leatest_news = Index.objects.filter().order_by('-Title')

    context = {
        'apply' : apply,
        'leatest' : leatest_news
    }

    return render (request, 'index.html', context=context)