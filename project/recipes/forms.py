# -*- coding: utf-8 -*-

from django import forms
from project.recipes.models import *

class RegisterForm(forms.Form):
    """User registration form"""
    name = forms.CharField(label=(u'Registracijos vardas'), max_length=100)
    email = forms.EmailField(label=(u'El. paštas'))
    psw = forms.CharField(label=(u'Slaptažodis'), widget=\
    forms.PasswordInput(render_value=False), max_length=100)
    psw2 = forms.CharField(label=(u'Patvirtinti slaptažodį'), widget=\
    forms.PasswordInput(render_value=False), max_length=100)
    
class LoginForm(forms.Form):
    """User login form"""
    name = forms.CharField(max_length=100, label="Vardas")
    psw = forms.CharField(label=(u'Slaptažodis'), widget=\
    forms.PasswordInput(render_value=False), max_length=100)
    
def all_recipe_types():
    """Return next recipe type choice."""
    for rtype in RecipeType.objects.all():
        yield (rtype, rtype)
    
def all_cusines():
    """Return next cusine choice."""
    for cusine in Cusine.objects.all():
        yield(cusine, cusine)

def all_cooking_types():
    """Return next cooking type."""
    for cooking_type in CookingType.objects.all():
        yield(cooking_type, cooking_type)
        
def all_complexities():
    """Return next complexity choice."""
    for complexity in Complexity.objects.all():
        yield(complexity, complexity)

class RecipeForm(forms.Form):
    """Cooking recipe form"""
    name = forms.CharField(label="Pavadinimas", max_length=200)
    process = forms.CharField(label="Gaminimo eiga", \
    widget=forms.widgets.Textarea(attrs={'rows':16, 'cols':60}))
    duration = forms.CharField(label="Gaminimo trukmė", max_length=200, \
    required=False)
    description = forms.CharField(label="Recepto apibūdinimas", \
    widget=forms.widgets.Textarea(attrs={'rows':4, 'cols':60}), required=False)
    recipe_type = forms.ChoiceField(label="Kategorija", \
    choices=all_recipe_types())
    cusine = forms.ChoiceField(label="Virtuvė", choices=all_cusines())
    cooking_type = forms.ChoiceField(label="Ruošimo būdas", \
    choices=all_cooking_types())
    complexity = forms.ChoiceField(label="Sudėtingumas", \
    choices=all_complexities())
    ingredients= forms.CharField(label="Ingredientai", \
    widget=forms.widgets.Textarea(attrs={'rows':2, 'cols':60}))
    items = forms.CharField(label="Prietaisai, indai, įrankiai", \
    widget=forms.widgets.Textarea(attrs={'rows':2, 'cols':60}), required=False)
    
def recipe_types_with_none():
    """Return next recipe type choice including no choice"""
    yield("", "-------")
    for rtype in RecipeType.objects.all():
        yield (rtype, rtype)

def cusines_with_none():
    """Return next cusine choice including no choice"""
    yield("", "------")
    for cusine in Cusine.objects.all():
        yield(cusine, cusine)

def cooking_types_with_none():
    """Return next cooking type including no choice"""
    yield("", "------")
    for cooking_type in CookingType.objects.all():
        yield(cooking_type, cooking_type)

def complexities_with_none():
    """Return next complexity choice including no choice"""
    yield("", "------")
    for complexity in Complexity.objects.all():
        yield(complexity, complexity)
        
def dates_with_none():
    """Return next data choice"""
    yield("", "------")
    yield(0, "Šiandienos")
    yield(1, "Nuo vakar")
    yield(2, "Šios savaitės")
    yield(3, "Šio mėnesio")
    
class SearchForm(forms.Form):
    """Form for recipes filter"""
    name = forms.CharField(label="Pavadinimas", max_length=200, required=False)
    author = forms.CharField(label="Autorius", max_length=200, required=False)
    duration = forms.CharField(label="Gaminimo trukmė", max_length=200, \
    required=False)
    date = forms.ChoiceField(label="Laikas", choices=dates_with_none(), \
    required=False)
    recipe_type = forms.ChoiceField(label="Kategorija", \
    choices=recipe_types_with_none(), required=False)
    cusine = forms.ChoiceField(label="Virtuvė", choices=cusines_with_none(), \
    required=False)
    cooking_type = forms.ChoiceField(label="Ruošimo būdas", \
    choices=cooking_types_with_none(), required=False)
    complexity = forms.ChoiceField(label="Sudėtingumas", \
    choices=complexities_with_none(), required=False)
    
class ChangePswForm(forms.Form):
    """User password change form"""
    psw = forms.CharField(label="Slaptažodis", widget=\
    forms.PasswordInput(render_value=False), max_length=200)
    newpsw1 = forms.CharField(label="Naujas slaptažodis", widget=\
    forms.PasswordInput(render_value=False), max_length=200)
    newpsw2 = forms.CharField(label="Patvirtinti slaptažodį", widget=\
    forms.PasswordInput(render_value=False), max_length=200)