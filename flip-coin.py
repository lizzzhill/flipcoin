import random

# Функция для подбрасывания монетки
def flip_coin():
    # Генерируем случайное число от 0 до 1
    result = random.randint(0, 1)
    # Если число равно 0, то выпал орел, иначе - решка
    if result == 0:
        return "Орел"
    else:
        return "Решка"

# Пример использования функции для подбрасывания монетки
result = flip_coin()
print(result)
