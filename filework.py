import os
from pprint import pprint

def cook_book_load(filename):
    cook_book = {}
    path = os.path.join(os.getcwd(), filename)
    with open(path, 'rt', encoding='utf-8') as f:
        for recipe in f:
            ing_count = int(f.readline())
            ingredients = []
            for i in range(ing_count):
                ingredient_name, quantity, measure = f.readline().strip().split(" | ")
                ingredients.append({'ingredient_name' : ingredient_name, 'quantity' : quantity, 'measure' : measure})
            f.readline()
            cook_book[recipe.strip()] = ingredients
    return cook_book

cook_book = cook_book_load("recipes.txt")

# pprint(cook_book,width=200)

def get_shop_list_by_dishes(dishes, person_count):
    ingredients = {}
    for dish in dishes:
        if dish in cook_book:
            ing = cook_book.get(dish)
            for i in ing:
                if i.get('ingredient_name') not in ingredients:
                    ingredients[i.get('ingredient_name')] = {
                       'measure' : f'{i.get("measure")}',
                       'quantity' : f'{float(i.get("quantity")) * person_count}'
                    }
                else:
                    quantity = float(ingredients[i.get('ingredient_name')].get('quantity')) + float(i.get("quantity")) * person_count
                    ingredients[i.get('ingredient_name')]['quantity'] = quantity
        else:
            return False
    return ingredients

# dishes = get_shop_list_by_dishes(list(cook_book.keys()), 3)
dishes = get_shop_list_by_dishes(['Омлет'], 2)
if dishes:
    pprint(dishes)
else:
    print("Нет такого блюда в книге рецептов")