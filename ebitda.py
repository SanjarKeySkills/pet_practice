def calculate_ebitda_basic(revenue, cogs, operating_expenses, depreciation, amortization):
    """
    Базовая формула EBITDA:
    EBITDA = Выручка - Себестоимость - Операционные расходы + Амортизация
    """
    ebitda = revenue - cogs - operating_expenses + depreciation + amortization
    return ebitda

# Пример использования
revenue = 1000000  # Выручка
cogs = 600000      # Себестоимость продаж
operating_expenses = 200000  # Операционные расходы
depreciation = 50000         # Амортизация ОС
amortization = 30000         # Амортизация НМА

ebitda = calculate_ebitda_basic(revenue, cogs, operating_expenses, depreciation, amortization)
print(f"EBITDA: {ebitda:,.2f}")  # EBITDA: 280,000.00

# ---------------------------------------
# Расчет через операционную прибыль (EBIT)


