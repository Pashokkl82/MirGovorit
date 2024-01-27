"""test_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.urls import include, path
import dish.views as views

urlpatterns = []

urlpatterns += [
    path('add_product_to_recipe/', views.AddProductToRecipe.as_view(), name='add-product-to-recipe'),
    path('cook_recipe/', views.CookRecipe.as_view(), name='cook-recipe'),
    path('show_recipes_without_product/', views.ShowRecipesWithoutProduct.as_view(), name='show-recipes-without-product'),
]
