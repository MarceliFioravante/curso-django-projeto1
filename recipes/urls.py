from django.urls import path

from . import views

# esse . (Ponto), mostra que a pasta views está na mesma pasta
# de recipes, ou seja, da pasta em que estou, import views

# dominio/recipes/
urlpatterns = [
    path('', views.home),
    path('recipes/<int:id>/', views.recipe),
]
