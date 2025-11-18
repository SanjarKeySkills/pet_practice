# farenheit = float(input("please isert your temperature"))
# celsius = (5/9) * (farenheit - 32)
# print(f"In Celsium it is: {celsius:.2f}")




# --------------------


# Конвертация USD -> другая валюта (например, KGS)

amount_usd = float(input("Введите сумму в долларах США: "))
rate = float(input("Введите курс доллара (сколько стоит 1 USD): "))

result = amount_usd * rate

print("Результат перевода:", result)