from django.http import Http404
from django.shortcuts import render
from utils.recipes.factory import make_recipe

from recipes.models import Recipe

# o render le um arquivo e renderiza o mesmo.
# O django procura arquivos HTML dentro de uma pasta de nome template


def home(request):
    recipes = Recipe.objects.filter(
        is_published=True
    ).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def category(request, category_id):
    recipes = Recipe.objects.filter(
        category__id=category_id,
        is_published=True,
    ).order_by('-id')

    '''category_name = getattr(
        getattr(recipes.first(), 'category', None),
        'name',
        'Not found'''''

    if not recipes:
        # return HttpResponse(content='Not found', status=404)
        raise Http404('Not found')

    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipe.first().category.name} - Category |',
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })
