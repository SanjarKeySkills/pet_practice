
from collections import Counter
sentence = str(input("Please insert your sentence:"))
print(sentence)

str = "If you want your classes to be reusable then you will find that different clients have different output requirements let the client not the class worry about the output side of things."

list = sentence.split()

object = Counter(list)
x = dict(object)
print(x)

# Пример использования
my_list = [1, 2, 3, 4, 5]
result = calculate_sum(my_list)
print(f"Сумма элементов списка: {result}") # Вывод: Сумма элементов списка: 15