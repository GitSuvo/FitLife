# Проект FitLife - MVP версия 1.0


# 1. Знакомство.

user_name = input('Здраствуйте, как к Вам обращаться? ')
user_age = int(input('Сколько Вам лет? '))

# 2. Сбор данных.

user_weight = float(input('Какой у Вас вес?(кг) '))
user_height = float(input('Какой у Вас рост?(м, например 1.75) '))

# 3. Расчеты ИМТ и (воды в литрах).

bmi = round((user_weight / (user_height ** 2)), 1)

stnd_lt_per_kg = 30
water_needed = round(((user_weight * stnd_lt_per_kg) / 1000), 1)

# 4. Вывод результата

print(f'Отчет для пользоателя: {user_name}')
print(f'Ваш индекс массы тела: {bmi}')
print(f'Рекомендуемая норма воды: {water_needed} л. в день.')
print("Расчет окончен. Будьте здоровы!")
