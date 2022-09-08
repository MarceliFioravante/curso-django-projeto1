from django.shortcuts import render

# o render le um arquivo e renderiza o mesmo.
# O django procura arquivos HTML dentro de uma pasta de nome template


def home(request):
    # return HttpResponse('HOME')
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Marceli',
    })


def recipe(request, id):
    # return HttpResponse('HOME')
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Marceli',
    })
