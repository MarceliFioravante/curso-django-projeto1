from django.shortcuts import render
from utils.recipes.factory import make_recipe

from recipes.models import Recipe

# o render le um arquivo e renderiza o mesmo.
# O django procura arquivos HTML dentro de uma pasta de nome template


def home(request):
    recipes = Recipe.objects.filter(
        is_published=True
    ).order_by('-id')
    # return HttpResponse('HOME')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def category(request, category_id):
    recipes = Recipe.objects.filter(
        category__id=category_id,
        is_published=True
    ).order_by('-id')
    # return HttpResponse('HOME')
    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
    })


def recipe(request, id):
    # return HttpResponse('HOME')
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })
