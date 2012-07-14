#-*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class ProductCategory(models.Model):
    imgProductCategory = models.FileField(upload_to="images/category/", blank=True,null=True)
    nameProductCategory = models.CharField(max_length = 200)
    parentID = models.ForeignKey('self', blank=True, null=True)
    
class Product(models.Model):
    categoryID = models.ForeignKey(ProductCategory)
    nameProduct = models.CharField(max_length = 200)
    price = models.DecimalField(decimal_places=2,max_digits=8)
    unit = models.IntegerField()
    imgProduct = models.FileField(upload_to="images/product/", blank=True,null=True)
    
class RecipeCatrgory(models.Model):
    nameRecipeCategory = models.CharField(max_length = 200)
    patentID = models.ForeignKey('self', blank=True, null=True)

class Recipe(models.Model):
    ADVANCE_STATUS = ((0, 'Łatwy'), (1, 'Średni'), (2, 'Zaawansowany'))
    categoryID = models.ForeignKey(RecipeCatrgory)
    nameRecipe = models.CharField(max_length = 200)
    timePrepare = models.IntegerField()
    level = models.SmallIntegerField(choices=ADVANCE_STATUS)
    imgFinishRecipe = models.FileField(upload_to="images/recipe/", blank=True,null=True)
    
class RecipeStep(models.Model):
    recipeID = models.ForeignKey(Recipe)
    discribeStep = models.CharField(max_length = 500)
    


    
    