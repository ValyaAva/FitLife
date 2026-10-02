# Проект FitLife - MVP версия 1.0
# Заставляем Python использовать UTF-8 для вывода в консоль
import io
import sys


sys.stdout = io.TextIOWrapper(
    sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.stderr = io.TextIOWrapper(
    sys.stderr.buffer, encoding="utf-8", errors="replace")
CONSTANT_ML = 1000
WATER_PER_KG = 30

print("Добро пожаловать в проект FitLife ")
print("Я ваш помощник по расчету ИМТ и нормы воды")

# Знакомство с пользователем

user_name = input("Как тебя зовут ? : ").capitalize()
user_age = int(input("Сколько тебе лет ? : "))

# Ввод данных о пользователе

user_weight = float(input("Введи свой вес (в кг) : "))
user_height = float(input("Введи свой рост (в метрах, например 1.75) : "))

# Расчет ИМТ


def calculate_bmi(weight, height):
    """Считает индекс массы тела (ИМТ)"""
    return weight / (height ** 2)


bmi = float(calculate_bmi(user_weight, user_height))
if bmi < 18.5:
    print(" Y вас недостаточный вес")
elif bmi > 24.9:
    print("У вас избыточный вес")
else:
    print("Ваш вес в норме")
print("Ваше ИМТ составляет : {:.1f}".format(bmi))

# Расчет нормы воды

def calculate_water(weight):
    """Считает норму воды в миллилитрах на основе веса тела"""
    return weight * WATER_PER_KG
water_needed = calculate_water(user_weight)/CONSTANT_ML


print(f"Привет, {user_name}!")
print(f"Возраст: {user_age},ИМТ: {round(bmi, 1)}")
print(f"Норма воды: {water_needed} л")
print("Расчет окончен. Будьте здоровы!")
