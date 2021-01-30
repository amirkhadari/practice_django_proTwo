from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# Create your views here.


def help(request):
    con = {'Ask_us': 'How Can i Help You!!!'}
    return render(request, 'help.html', context=con)


def our_team(request):
    teams = User.objects.order_by('first_name')
    contacts = {'team_list': teams}
    return render(request, 'team.html', context=contacts)
