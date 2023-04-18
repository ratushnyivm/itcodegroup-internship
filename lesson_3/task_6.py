# Определить, является ли число простым.
# Напишите программу, которая на вход принимает любое не отрицательное число, а
# выводит строку «Простое» или же «Составное», в случае, если число не является
# простым.

number = 62


def is_prime(number: int) -> bool:
    if number % 2 == 0 or number == 1:
        return number == 2

    divisor = 3
    while divisor * divisor <= number and number % divisor != 0:
        divisor += 2

    return divisor * divisor > number


def get_message(number: int) -> str:
    return 'Простое' if is_prime(number) else 'Составное'


if __name__ == '__main__':
    print(get_message(number))
