# -*- coding: utf-8 -*-

from django.db import models
from datetime import datetime, timedelta

class Recipe(models.Model):
    """Recepto įrašui saugoti skirta klasė"""
    name = models.CharField(max_length=200, null=True) # Pavadinimas
    author = models.CharField(max_length=200, null=True) # Autorius
    process = models.TextField(null=True) # Gaminimo eiga
    duration = models.CharField(max_length=200, null=True) # Gaminimo trukme
    description = models.TextField(null=True) # Patiekalo apibudinimas
    pub_date = models.DateTimeField('sukūrimo laikas', null=True) # Data
    recipe_type = models.ForeignKey('RecipeType', null=True) # pvz.: desertas
    cusine = models.ForeignKey('Cusine', null=True)  # Virtuvė, pvz.: italų
    cooking_type = models.ForeignKey('CookingType', null=True) # pvz.: virimas
    complexity = models.ForeignKey('Complexity', null=True) # Sudėtingumas
    ingredients = models.TextField(null=True) # Reikalingi produktai
    items = models.TextField(null=True) # Reikalingos priemonės
    def __unicode__(self):
        return self.name
        
    @classmethod
    def search(self, name, author, duration, date, rt, cusine, ct, comp):
        """Grąžink filtruotą pagal nurodytus kriterijus receptų sąrašą"""
        recipe_list = []        
        print name, author, duration, date, rt, cusine, ct, comp
        for recipe in Recipe.objects.all():
            if ((name == None)|(recipe.name.lower().find(name.lower()) != -1))&\
            ((author == None)|(str(recipe.author.lower()).find(author.lower()) \
            != -1))&\
            ((not rt)|(str(recipe.recipe_type) == rt))&\
            ((not cusine)|(str(recipe.cusine) == cusine))&\
            ((not ct)|(str(recipe.cooking_type) == ct))&\
            ((not comp)|(str(recipe.complexity) == comp))&\
            ((duration == None)|(str(recipe.duration.lower()).find(\
            duration.lower()) != -1))&\
            ((not date)|((date == '0')&(recipe.pub_date.date()==\
            datetime.now().date()))|\
            ((date == '1')&(recipe.pub_date.date()>=\
            datetime.now().date()-timedelta(days=1)))|\
            ((date == '2')&(recipe.pub_date.date()>=\
            datetime.now().date()-timedelta(days=7)))|\
            ((date == '3')&(recipe.pub_date.date()>=\
            datetime.now().date()-timedelta(days=30)))):
                recipe_list.append(recipe)
        return recipe_list
        
class RecipeType(models.Model):
    "Recepto tipui (pvz.: sriuba, salotos) saugoti skirta klasė"
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name
        
class Cusine(models.Model): # Cuisine
    "Virtuvei (pvz.: italų, kiniečių) saugoti skirta klasė"
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class CookingType(models.Model):
    "Maisto ruošimo būdui (pvz.: virimas, kepimas) saugoti skirta klasė"
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name
        
class Complexity(models.Model):
    "Recepto sudėtingumui saugoti skirta klasė"
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name
    

