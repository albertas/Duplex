# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from project.recipes.forms import *
from project.recipes.models import *
from django.contrib.auth.decorators import login_required
from datetime import datetime
import random
from django.db import IntegrityError

def index(request):
    login_message = None
    if request.GET.get('next'):
        login_message = "Turite prisijungti"
    recipe = None
    if Recipe.objects.all():
        recipe = Recipe.objects.all()[random.randint(0, \
        len(Recipe.objects.all())-1)]
    latest_recipe_list = Recipe.objects.all().order_by('-pub_date')[:5]
    if request.user.is_authenticated():
        return render_to_response('index.html', {'user': request.user, \
        'latest_recipe_list': latest_recipe_list, 'recipe': recipe, \
        'login_message': login_message })
    login_form = LoginForm()
    return render_to_response('index.html', {'login_form': login_form, \
    'latest_recipe_list': latest_recipe_list, 'recipe': recipe,\
    'login_message': login_message })
        
def register(request):
    rlist = Recipe.objects.all().order_by('-pub_date')[:5]
    recipe = None
    if Recipe.objects.all():
        recipe = Recipe.objects.all()[random.randint(0, \
        len(Recipe.objects.all())-1)]
    if request.method == 'POST': 
        form = RegisterForm(request.POST) 
        if form.is_valid(): 
            if form.cleaned_data['psw'] != form.cleaned_data['psw2']:
                return render_to_response('user/register.html', \
                {'register_form': form, 'error_message': \
                'Slaptažodžiai nesutampa', 'latest_recipe_list': rlist})
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            try:
                User.objects.create_user(name, email, form.cleaned_data['psw'])
                user = authenticate(username=name, \
                password=form.cleaned_data['psw'])
                login(request, user)
            except IntegrityError:
                return render_to_response('user/register.html', \
                {'register_form': form, 'error_message': \
                'Toks registracijos vardas jau egzistuoja', \
                'latest_recipe_list': rlist})
            return render_to_response('index.html', {'user': user, \
            'latest_recipe_list': rlist, 'recipe': recipe })
    else:
        form = RegisterForm() 
    return render_to_response('user/register.html', {'register_form': form, \
    'latest_recipe_list': rlist, 'recipe': recipe})
    
def userlogin(request):
    latest_recipe_list = Recipe.objects.all().order_by('-pub_date')[:5]
    recipe = None
    if Recipe.objects.all():
        recipe = Recipe.objects.all()[random.randint(0, \
        len(Recipe.objects.all())-1)]
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['name']
            password = form.cleaned_data['psw']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render_to_response('index.html', {"user": user, \
                    'latest_recipe_list': latest_recipe_list, \
                    'recipe': recipe })
                else:
                    print "User is not active"
                    login_form = LoginForm()
                    return render_to_response('index.html', {"user": user, \
                    'latest_recipe_list': latest_recipe_list, \
                    'recipe': recipe,'login_message': 'Bandykite dar kartą' })
            else:
                login_form = LoginForm()
                return render_to_response('index.html', {'login_form': \
                login_form, 'latest_recipe_list': latest_recipe_list, \
                'recipe': recipe, 'login_message': 'Bandykite dar kartą' })
        else:
            login_form = form
    else:        
        login_form = LoginForm()
    return render_to_response('index.html', {"login_form": login_form, \
    'latest_recipe_list': latest_recipe_list, 'recipe': recipe,\
    'login_message': 'Bandykite dar kartą' })
            
def kontaktai(request):
    latest_recipe_list = Recipe.objects.all().order_by('-pub_date')[:5]
    login_form = LoginForm()
    return render_to_response('contacts.html', {'user': request.user, \
    'latest_recipe_list': latest_recipe_list, 'login_form': login_form })
    
@login_required
def kurimas(request):
    latest_recipe_list = Recipe.objects.all().order_by('-pub_date')[:5]
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            author = str(request.user)
            process = form.cleaned_data['process']
            duration = form.cleaned_data['duration']
            description = form.cleaned_data['description']
            pub_date = datetime.now()
            recipe_type = RecipeType.objects.get(name=\
            form.cleaned_data['recipe_type'])
            cusine = Cusine.objects.get(name=form.cleaned_data['cusine'])
            cooking_type = CookingType.objects.get(name=\
            form.cleaned_data['cooking_type'])
            complexity = Complexity.objects.get(name=\
            form.cleaned_data['complexity'])
            ingredients = form.cleaned_data['ingredients']
            items = form.cleaned_data['items']
            recipe = Recipe(name=name, author=author, process=process, \
            duration=duration, description=description, pub_date=pub_date, \
            recipe_type=recipe_type, cusine=cusine, cooking_type=cooking_type,\
            complexity=complexity, ingredients=ingredients, items=items)
            recipe.save()
            new_form = RecipeForm()
            return HttpResponseRedirect('/receptas/'+str(recipe.pk)+'/')
    else:
        form = RecipeForm()
    return render_to_response('create.html', {'user': request.user, \
    'form': form, 'latest_recipe_list': latest_recipe_list})

def sarasas(request, recipe_list=None):
    latest_recipe_list = Recipe.objects.all().order_by('-pub_date')[:5]
    if not recipe_list:
        recipe_list = Recipe.objects.all().order_by('-pub_date')
    form = LoginForm()
    return render_to_response('list.html', {'recipe_list': recipe_list, \
    'user':request.user, 'latest_recipe_list': latest_recipe_list, \
    'login_form': form})

def paieska(request):
    latest_recipe_list = Recipe.objects.all().order_by('-pub_date')[:5]
    form = LoginForm()
    if request.method == 'POST': 
        search_form = SearchForm(request.POST) 
        if search_form.is_valid():
            name = search_form.cleaned_data['name']
            author = search_form.cleaned_data['author']
            duration = search_form.cleaned_data['duration']
            date = search_form.cleaned_data['date']
            recipe_type = search_form.cleaned_data['recipe_type']
            cusine = search_form.cleaned_data['cusine']
            cooking_type = search_form.cleaned_data['cooking_type']
            complexity = search_form.cleaned_data['complexity']
            recipe_list = Recipe.search(name, author, duration, date, \
            recipe_type, cusine, cooking_type, complexity)
            return render_to_response('list.html', {'recipe_list': \
            recipe_list, 'user':request.user, \
            'latest_recipe_list': latest_recipe_list, 'login_form': form})
    else:
        search_form = SearchForm()
    return render_to_response('search.html', {'search_form': search_form, \
    'user':request.user, 'latest_recipe_list': latest_recipe_list, \
    'login_form': form})
 
@login_required   
def userlogout(request):
    latest_recipe_list = Recipe.objects.all().order_by('-pub_date')[:5]
    recipe = None
    if Recipe.objects.all():
        recipe = Recipe.objects.all()[random.randint(0, \
        len(Recipe.objects.all())-1)]
    logout(request)
    login_form = LoginForm()
    return render_to_response('index.html', {'login_form': login_form, \
    'latest_recipe_list': latest_recipe_list, 'recipe': recipe })
    
def receptas(request, recipe_id):
    latest_recipe_list = Recipe.objects.all().order_by('-pub_date')[:5]
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    login_form = LoginForm()
    return render_to_response('recipe.html', {'user': request.user, \
    'recipe': recipe, 'latest_recipe_list': latest_recipe_list, \
    'login_form': login_form})
    
def changepsw(request):
    latest_recipe_list = Recipe.objects.all().order_by('-pub_date')[:5]
    recipe = None
    if Recipe.objects.all():
        recipe = Recipe.objects.all()[random.randint(0, \
        len(Recipe.objects.all())-1)]
    if request.method == 'POST': 
        form = ChangePswForm(request.POST) 
        if form.is_valid():
            psw = form.cleaned_data['psw']
            npsw1 = form.cleaned_data['newpsw1']
            npsw2 = form.cleaned_data['newpsw2']
            user = request.user
            if npsw1 != npsw2:
                return render_to_response('user/changepsw.html', \
                {'changepsw_form': form, 'error_message': \
                'Slaptažodžiai nesutampa', 'latest_recipe_list': \
                latest_recipe_list, 'user': request.user})
            if user.check_password(psw):
                user.set_password(npsw1)
                user.save()
            else:
                return render_to_response('user/changepsw.html', \
                {'changepsw_form': form, 'error_message': \
                'Neteisingas slaptažodis', 'latest_recipe_list': \
                latest_recipe_list, 'user': request.user})
            form = ChangePswForm()
            return render_to_response('user/changepsw.html', \
            {'changepsw_form': form, 'latest_recipe_list': latest_recipe_list,\
            'recipe': recipe, 'user': request.user, 'error_message': \
            'Slaptažodis pakeistas'})
    else:
        form = ChangePswForm() 
    return render_to_response('user/changepsw.html', {'changepsw_form': form, \
    'latest_recipe_list': latest_recipe_list, 'recipe': recipe, 'user': \
    request.user})