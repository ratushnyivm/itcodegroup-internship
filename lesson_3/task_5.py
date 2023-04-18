# Нужно вывести наименование продукта только, если количество букв в
# нем четное.
# Пройдитесь циклом по списку и выведи название каждого такого продукта.

products = [
    'Apple', 'Milk', 'Bread', 'Chicken', 'Cheese',
    'Carrots', 'Rice', 'Tomatoes', 'Eggs', 'Yogurt'
]

if __name__ == '__main__':
    for product in products:
        if len(product) % 2 == 0:
            print(product)
