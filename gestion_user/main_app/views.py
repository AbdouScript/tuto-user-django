from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User,Session

# Create your views here.
def index(request):
    list_users = User.objects.all()
    list_sessions = Session.objects.all()
    template = loader.get_template('main_app/index.html')
    context = {
        'list_users': list_users,
        'list_sessions':list_sessions,
    }
    return HttpResponse(template.render(context, request))

def users(request):
    list_users = User.objects.all()
    template = loader.get_template('main_app/users.html')
    context = {
        'list_users': list_users,
    }
    return HttpResponse(template.render(context, request))

def sessions(request):
    list_sessions = Session.objects.all()
    template = loader.get_template('main_app/sessions.html')
    context = {
        'list_sessions': list_sessions,
    }
    return HttpResponse(template.render(context, request))

def details(request,user_id):
    utilisateur = User.objects.get(pk=1)
    # list_sessions = utilisateur.session_set.all
    return render(request, 'main_app/detail.html', {'user': utilisateur})