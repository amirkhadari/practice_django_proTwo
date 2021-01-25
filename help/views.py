from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def help(request):
    con = {'Ask_us': 'How Can i Help You!!!'}
    return render(request, 'help.html', context=con)
