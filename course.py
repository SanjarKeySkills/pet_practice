# x = 1
# y = 2
# unit_price = 3

# print("Hello World!")

def calculate_sum(numbers):
  """
  Алгоритм для вычисления суммы всех чисел в списке.

  :param numbers: Список чисел.
  :return: Сумма чисел в списке.
  """
  total = 0  # Шаг 1: Инициализировать переменную для суммы
  for number in numbers:  # Шаг 2: Повторять для каждого числа в списке
    total += number  # Шаг 3: Прибавить текущее число к сумме
  return total  # Шаг 4: Вернуть итоговую сумму

# Пример использования
my_list = [1, 2, 3, 4, 5]
result = calculate_sum(my_list)
print(f"Сумма элементов списка: {result}") # Вывод: Сумма элементов списка: 15

# Пример использования
my_lis2t = [1, 2, 3, 4, 5]
result2 = calculate_sum(my_list)
print(f"Сумма элементов списка: {result2}") # Вывод: Сумма элементов списка: 15