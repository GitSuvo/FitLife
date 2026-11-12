# Проект FitLife - MVP версия 1.0

# Константы:

STND_ML_PER_KG = 30
CONV_ML_TO_LT = 1000

# 1. Знакомство.

user_name = input('Здраствуйте, как к Вам обращаться? ').strip()
while True:
    try:
        user_age = int(input('Сколько Вам лет? '))
        break
    except ValueError:
        print('Пожалуйста, введите корректное целое число, например, 25.')

# 2. Сбор данных.
while True:
    try:
        user_weight = float(input('Какой у Вас вес?(кг) '))
        break
    except ValueError:
        print('Пожалуйста, введите корректное число, например, 60.5 (используя точку) или 60.')

while True:
    try:
        user_height = float(input('Какой у Вас рост?(м, например 1.75) '))
        break
    except ValueError:
        print('Пожалуйста, введите корректное число, например, 1.75 (используя точку).')
    
        

# 3. Расчеты ИМТ и (воды в литрах).

bmi = round((user_weight / (user_height ** 2)), 1)
water_needed = round(((user_weight * STND_ML_PER_KG) / CONV_ML_TO_LT), 1)

# 4. Вывод результата

print(f'Отчет для пользоателя: {user_name}')
print(f'Ваш индекс массы тела: {bmi}')
print(f'Рекомендуемая норма воды: {water_needed} л. в день.')
print('Расчет окончен. Будьте здоровы!')
