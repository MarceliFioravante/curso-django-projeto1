from django.urls import path

from . import views

# recipes:recipe
app_name = 'recipes'

# esse . (Ponto), mostra que a pasta views está na mesma pasta
# de recipes, ou seja, da pasta em que estou, import views

# dominio/recipes/
urlpatterns = [
    path('', views.home, name="home"),
    path('recipes/category/<int:category_id>/',
         views.category, name="category"),
    path('recipes/<int:id>/', views.recipe, name="recipe"),
    path('recipes/search/', lambda request: ..., name="search"),

]
