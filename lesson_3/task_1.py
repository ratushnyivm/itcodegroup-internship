# Напечатайте на экран сообщение о текущей дате и погоде в этот день
# в следующем формате:
# Сегодня … …. На улице … градусов.
# День хранится в переменной day, месяц - month.
# Температура хранится в переменной temperature.
# Если температура ниже нуля, то добавьте следующий строкой:
# «Холодно, лучше остаться дома».

day = '12'
month = 'февраль'
temperature = -10


def get_date_and_weather(day: str, month: str, temp: int) -> str:
    month = f'{month}а' if month in ('март', 'август') else f'{month[:-1]}я'
    msg = f'Cегодня {day} {month}. На улице {temp} градусов.'

    if temp < 0:
        return msg + '\nХолодно, лучше остаться дома.'

    return msg


if __name__ == '__main__':
    print(get_date_and_weather(day, month, temperature))
