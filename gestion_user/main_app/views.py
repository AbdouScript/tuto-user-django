from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import User,Session

from .formulaire import form_auth

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

def authentification(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = form_auth(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('app/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = form_auth()

    return render(request, 'name.html', {'form': form})