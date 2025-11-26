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

def calculate_ebitda_from_ebit(ebit, depreciation, amortization):
    """
    EBITDA = EBIT + Амортизация ОС + Амортизация НМА
    """
    return ebit + depreciation + amortization

# Пример
ebit = 200000  # Операционная прибыль
depreciation = 50000
amortization = 30000

ebitda = calculate_ebitda_from_ebit(ebit, depreciation, amortization)
print(f"EBITDA: {ebitda:,.2f}")

# ------------------------------------------------
