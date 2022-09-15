from django.shortcuts import render
from utils.recipes.factory import make_recipe

# o render le um arquivo e renderiza o mesmo.
# O django procura arquivos HTML dentro de uma pasta de nome template


def home(request):
    # return HttpResponse('HOME')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': [make_recipe() for _ in range(10)],
    })


def recipe(request, id):
    # return HttpResponse('HOME')
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
    })
