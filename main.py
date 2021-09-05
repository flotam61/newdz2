from pprint import pprint

def prepare_dict(file_name: str) -> dict:
    result: dict = dict()

    with open(file_name, "r", encoding="UTF-8") as file:
        for line in file:
            ingredient_name = line.strip()
            quantity = int(file.readline())
            cook_book = []
            for recept in range(quantity):
                name, quantityrec, value = file.readline().strip().split("|")
                cook_book.append({"name": name, "number": int(quantityrec), "value": value})
            result[ingredient_name] = cook_book
            file.readline()
    return result

result_dict = prepare_dict("recept.txt")


def get_shop_list_by_dishes(dishes, person_count):

    for dish in dishes:
        for key in result_dict[dish]:
            list_item = dict(key)
            list_item["number"] *= person_count
            print(list_item)


get_shop_list_by_dishes(['Запеченный картофель', "Омлет"], 5)


