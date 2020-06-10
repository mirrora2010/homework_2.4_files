def open_file(file_name):
    file_lines = []
    with open(file_name, 'r', encoding='utf8') as file:
        for line in file:
            file_lines.append(line.rstrip())
    return file_lines

def get_cook_book(file_name):
    recipes_list = open_file(file_name)

    dish = []
    cook_book = {}
    recipes_list.append('')

    for items in recipes_list:
        if items != '':
            dish.append(items)
        else:
            another_dish = dish.copy()
            another_dish.pop(0)
            another_dish.pop(0)

            ingredients_list = []
            for string in another_dish:
                dict = {}
                string = string.split(" | ")
                dict["ingredient_name"] = string[0]
                dict["quantity"] = string[1]
                dict["measure"] = string[2]
                ingredients_list.append(dict)

            cook_book[dish[0]] = ingredients_list
            dish = []

    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = get_cook_book('cookbook.txt')
    print(cook_book)
    dict_of_ingredients = {}
    list_of_ingredients = []
    for dish in dishes:
        try:
            for ingredient in cook_book.get(dish):
                ingredient_name = ingredient.get('ingredient_name')
                measure = ingredient.get('measure')
                if ingredient['ingredient_name'] not in list_of_ingredients:
                    quantity = int(ingredient.get('quantity')) * person_count
                    dict_of_ingredients.update({ingredient_name: {'measure': measure, 'quantity': quantity}})
                    list_of_ingredients.append(ingredient['ingredient_name'])
                else:
                    quantity = int(ingredient.get('quantity')) * person_count + dict_of_ingredients[ingredient_name][
                        'quantity']
                    dict_of_ingredients.update({ingredient_name: {'measure': measure, 'quantity': quantity}})
        except TypeError as e:
            print(f'В книге рецептов нет блюда под названием "{dish}" или название написано с ошибкой.')
    print(dict_of_ingredients)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
#get_shop_list_by_dishes(['Амлет'], 2)









