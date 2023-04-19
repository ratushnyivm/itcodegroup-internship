# Посчитаем количество наименований продуктов, которые нужно сегодня купить.
# Создайте список, содержащий названия продуктов.
# Объявите переменную count и посчитайте в ней количество продуктов
# Выведите на экран сообщение в формате:
# У тебя {количество} продуктов, где {количество} — значение переменной count.

from typing import List

products = [
    'Apple', 'Milk', 'Bread', 'Chicken', 'Cheese',
    'Carrots', 'Rice', 'Tomatoes', 'Eggs', 'Yogurt'
]


def count_products(products_list: List[str]) -> str:
    count = len(products_list)
    return f'У тебя {count} продуктов, ' \
           f'где {count} — значение переменной count.'


if __name__ == '__main__':
    print(count_products(products))
