from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import User,Session
from .forms import FormConnexion

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

# def inscription(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = form_auth(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('app/inscription/')

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = form_auth()

#     return render(request, 'name.html', {'form': form})

def register(request):
    if request.method == 'POST':
        user = User()
        print(request.POST['nom'])
        user.nom = request.POST['nom']
        user.prenom = request.POST['prenom']
        user.email_user = request.POST['email_user']
        user.password = request.POST['password']
        user.save()
        return HttpResponseRedirect('/connexion/')
    else :
        error = 'erreur d\'inscription'

        context = {'error':error}
        return render(request, 'main_app/inscription.html',context)
        # return HttpResponse(template.render(context, request))

def profil(request,user_id):
    if(User.objects.filter(pk=user_id)):
        user = User.objects.get(pk=user_id)
        context = {
        'user': user,
        }
        # return HttpResponse('Votre profil est enregistré, votre nom est %s' % str(user.nom))
        return render(request, 'main_app/profil.html', context)
    else :
        return HttpResponse('erreur d\'affichage du profil')
    
# def connexion(request):
#     if request.method == 'POST':
        
#         return HttpResponseRedirect('/connexion/')
#     else :
#         error = 'erreur de connexion'

#         context = {'error':error}
#         return render(request, 'main_app/inscription.html',context)

def connexion(request):
    context={
         'form':'',
        'message':'Bienvenue dans la page de connexion'
    }

    if request.method =="POST":
        form =FormConnexion(request.POST)
        if form.is_valid():
            
            user=User.objects.get(email_user=form.cleaned_data['email_user'])
          
            if(user.password == form.cleaned_data['password']):
                url = "/app/"+str(user.id) + "/profil/"
                return HttpResponseRedirect(url)
    else:

        form=FormConnexion()
        context={
            'form':form,
            'message':'Bienvenue dans la page de connexion'
        }
        
    return render (request, 'main_app/connexion.html', {"context":context})