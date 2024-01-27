from rest_framework import generics, status
from rest_framework.response import Response
from .models import *
from django.shortcuts import render
from django.db.models import Q


class AddProductToRecipe(generics.ListAPIView):
    """Представление добавляет к указанному рецепту указанный продукт с указанным весом, если его нет.
        Если он есть, меняет его вес.
    """
    def get(self, request, *args, **kwargs):  # pylint: missing-function-docstring, unused-argument
        structure_record = Structure.objects.filter(recipe_id=request.query_params.get('recipe_id'))

        if structure_record.all().exists():  # Проверка на наличие запрашеваемого рецепта из запроса в БД
            product = Product.objects.filter(uuid=request.query_params.get('product_id'))
            if product:  # Проверка на наличие запрашеваемого продукта из запроса в БД
                record = Structure.objects.filter(recipe_id=request.query_params.get('recipe_id'), Product_id=request.query_params.get('product_id'))
                if record:  # Проверяем есть ли в рецепте уже такой продукт
                    record.Weight = request.query_params.get('weight')
                    record.save()
                    text = "Заменен вес продукта в рецепте"
                else:
                    record = Structure(Weight=request.query_params.get('weight'), Product_id=request.query_params.get('product_id'), recipe_id=request.query_params.get('recipe_id'))
                    record.save()
                    text = "Продукт и вес продукта добавлен в рецепт"
            else:
                text = "Такого продукта нет в БД"
                return Response(text, status=status.HTTP_404_NOT_FOUND)
        else:
            text = "Такого рецепта нет в БД!"
            return Response(text, status=status.HTTP_404_NOT_FOUND)

        return Response(text, status=status.HTTP_200_OK)


class CookRecipe(generics.ListAPIView):
    """Представление увеличивает на единицу количество приготовленных блюд для каждого продукта, входящего
    в указанный рецепт"""
    def get(self, request, *args, **kwargs):  # pylint: missing-function-docstring, unused-argument
        components = Structure.objects.filter(recipe_id=request.query_params.get('recipe_id'))
        if components.all().exists():  # Проверка на наличие запрашеваемого рецепта из запроса в БД
            for component in components:  # Перебираем компоненты входящие в запрашиваемый рецепт из запроса
                products = Product.objects.filter(uuid=component.Product_id)  # Находим список продуктов, колличество котрых будем увеличивать на 1
                for product in products:
                    product.number += 1
                    product.save()
            text = "Увеличено на единицу количество приготовленных блюд для каждого продукта, входящего в указанный рецепт."
            return Response(text, status=status.HTTP_200_OK)
        else:
            text = "Такого рецепта нет в БД!"
            return Response(text, status=status.HTTP_404_NOT_FOUND)


class ShowRecipesWithoutProduct(generics.ListAPIView):
    """
    Представление возвращает HTML страницу, на которой размещена таблица. В таблице отображены id и названия всех рецептов,
    в которых указанный продукт отсутствует, или присутствует в количестве меньше 10 грамм.
    """
    def get(self, request, *args, **kwargs):
        context = {}
        recipes = {}
        structure_records = Structure.objects.filter(Weight__lt=10) | Structure.objects.exclude(Product_id=request.query_params.get('product_id'))
        for record in structure_records:
            recipes[record.recipe_id] = Recipe.objects.get(uuid=record.recipe_id)

        context = {'recipes' : recipes}

        return render(request, 'recipes/start_page.html', context)
