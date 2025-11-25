# Формула: скорость = расстояние / время
def calculate_speed(distance, time):
    """
   Args:
        distance (float): Расстояние
        time (float): Время   
    Returns:
        float: Скорость
    """
    if time == 0:
        raise ValueError("Время не может быть равно нулю")
    return distance / time

# Примеры использования:
# Пример 1: автомобиль проехал 150 км за 2 часа
distance = 150  # км
time = 2        # часа
speed = calculate_speed(distance, time)
print(f"Скорость: {speed} км/ч")  # Вывод: Скорость: 75.0 км/ч

# Пример 2: пешеход прошел 5 км за 1.5 часа
distance2 = 5
time2 = 1.5
speed2 = calculate_speed(distance2, time2)
print(f"Скорость: {speed2} км/ч")  # Вывод: Скорость: 3.33 км/ч

# Альтернативный вариант - прямая формула:
def speed_formula(d, t):
    return d / t

# Использование:
result = speed_formula(100, 2)  # 100 км за 2 часа
print(f"Скорость: {result} км/ч")  # Вывод: Скорость: 50.0 км/ч
