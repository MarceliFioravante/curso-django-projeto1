from django.http import HttpResponse
from django.shortcuts import render

# o render le um arquivo e renderiza o mesmo. O django procura arquivos HTML dentro de uma pasta
# de nome template


def home(request):
    # return HttpResponse('HOME')
    return render(request, 'recipes/home.html', context={
        'name': 'Marceli',
    })


def contato(request):
    return HttpResponse('CONTATO')


def sobre(request):
    return HttpResponse('SOBRE views')
