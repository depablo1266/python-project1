user_name = input("Привет, как тебя зовут?")
print(
    f"Привет, {' '.join(user_name.split())}! "
    f"Добро пожаловать в фитнес-трекер!"
)

# Безопасный ввод возраста (целое число)
while True:
    try:
        user_age = int(input("Сколько тебе лет?"))
        break
    except ValueError:
        print("Пожалуйста, введи корректное число для возраста.")

# Безопасный ввод веса
while True:
    try:
        user_weight = float(input("Сколько ты весишь? (укажи в килограммах)"))
        break
    except ValueError:
        print("Ошибка! Введите вес числом (например: 75 или 74.5).")

# Безопасный ввод роста
while True:
    try:
        user_height = float(
            input(
                "Какой у тебя рост? "
                "(укажи в метрах через точку, например: 1.75)"
            )
        )
        break
    except ValueError:
        print("Ошибка! Введите рост числом (например: 1.75).")

print(f"Спасибо за информацию, {' '.join(user_name.split())}!")


# расчёт индекса массы тела
def calculate_bmi(weight, height):
    bmi = weight / (height**2)
    bmi = round(bmi, 1)
    return bmi


# расчёт необходимого потребления воды
def calc_water_ml(weight):
    water_per_kg = 30
    water_ml_per_l = 1000
    water_ml = weight * water_per_kg
    water_l = water_ml / water_ml_per_l
    return water_l


bmi = calculate_bmi(user_weight, user_height)
water_intake = calc_water_ml(user_weight)

# вывод отчета для пользователя
print(f"Отчет для пользователя {' '.join(user_name.split())}:")
print(f"Твой индекс массы тела (ИМТ) составляет: {bmi}")
print(f"Тебе нужно выпивать примерно {water_intake} литров воды в день.")
print(
    f"Спасибо, что воспользовались нашим фитнес-трекером, "
    f"{' '.join(user_name.split())}! "
    f"Удачи в достижении поставленных целей!"
)
