from pprint import pprint
def open_file(cookbook):
    file_lines = []
    with open('cookbook.txt', 'r', encoding='utf8') as file:
        for line in file:
            file_lines.append(line.rstrip())
    return file_lines

def get_cook_book(recipes_list):
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

            ingrediesnts_list = []
            for string in another_dish:
                dict = {}
                string = string.split(" | ")
                dict["ingredient_name"] = string[0]
                dict["quantity"] = string[1]
                dict["measure"] = string[2]
                ingrediesnts_list.append(dict)

            cook_book[dish[0]] = ingrediesnts_list
            dish = []

    return cook_book

cookbook = get_cook_book(open_file('cookbook.txt'))
#pprint (cookbook)

for key in cookbook:
    print(key, end=", ")
print()

chosen_dish = input('Введите название блюда из перечисленных выше: ').capitalize()
dishes = chosen_dish.split(',')
person_count = int(input("Введите количество порций: "))
#print(dishes)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    shop_list_extended = {}
    for dish in cookbook:
        if dish in dishes:
            for k in cookbook.get(dish):

                items = {}
                items['measure'] = k.get('measure')
                items['quantity'] = person_count * int(k.get('quantity'))
                ingredient = k.get('ingredient_name')
                shop_list_extended[ingredient] = items

            for item in shop_list_extended:

                if item in shop_list:
                    dic_a = shop_list_extended.get(item)
                    dic_b = shop_list.get(item)
                    qua_a = dic_a.get('quantity')
                    qua_b = dic_b.get('quantity')
                    com_measure = dic_b.get('measure')
                    combined = {}
                    combined["measure"] = com_measure
                    combined["quantity"] = int(qua_a) + int(qua_b)
                    shop_list[item] = combined

                else:
                    shop_list[item] = shop_list_extended.get(item)

    return shop_list

print(get_shop_list_by_dishes(dishes, person_count))


