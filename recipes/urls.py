from django.urls import path

from recipes.views import home

# dominio/recipes/
urlpatterns = [
    # path('sobre/', sobre),
    # path('contato/', contato),
    path('', home)  # as aspas vazias representam a raiz do site
]
