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
# ООП подход с классом Company
class Company:
    def __init__(self, name, revenue, cogs, operating_expenses, depreciation, amortization):
        self.name = name
        self.revenue = revenue
        self.cogs = cogs
        self.operating_expenses = operating_expenses
        self.depreciation = depreciation
        self.amortization = amortization
    
    @property
    def ebit(self):
        """Операционная прибыль (EBIT)"""
        return self.revenue - self.cogs - self.operating_expenses
    
    @property
    def ebitda(self):
        """EBITDA"""
        return self.ebit + self.depreciation + self.amortization
    
    def financial_report(self):
        """Генерация финансового отчета"""
        return f"""
Финансовый отчет: {self.name}
Выручка: {self.revenue:,.2f}
Себестоимость: {self.cogs:,.2f}
Операционные расходы: {self.operating_expenses:,.2f}
EBIT: {self.ebit:,.2f}
Амортизация ОС: {self.depreciation:,.2f}
Амортизация НМА: {self.amortization:,.2f}
EBITDA: {self.ebitda:,.2f}
"""

# Использование
company = Company(
    name="ТехноКорп",
    revenue=1500000,
    cogs=800000,
    operating_expenses=300000,
    depreciation=60000,
    amortization=40000
)

print(company.financial_report())

# --------------------------------
# Работа с pandas для анализа нескольких компаний