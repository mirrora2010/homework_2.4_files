# Задача №2
# Нужно написать функцию, которая на вход принимает список блюд из cook_book и количество персон для кого мы будем готовить
# get_shop_list_by_dishes(dishes, person_count)
# На выходе мы должны получить словарь с названием ингредиентов и его количества для блюда.

cook_book = {}

def get_cook_book():
    with open('cookbook.txt', 'r', encoding='utf8') as file:
        while True:
            recipe_name = file.readline().strip()
            if recipe_name.strip() == '':
                break
            number_of_ingredients = int(file.readline().strip())
            list_of_ingredients = []
            for i in range(number_of_ingredients):
                ingredient = file.readline().strip().split(' | ')
                ingredients = {'ingredient_name': ingredient[0], 'quantity': int(ingredient[1]),
                               'measure': ingredient[2]}
                list_of_ingredients.append(ingredients)
                cook_book.update({recipe_name: list_of_ingredients})
    print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            new_shop_list_item = dict(ingredient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingredient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
    print(shop_list)

