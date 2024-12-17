from django.shortcuts import render
from index.models import events

# Create your views here.


def index(request):
    list = events.objects.all().values('title')
    return render(request, 'senti_analysis.html',{'form':list})