# def calculate_ebitda_basic(revenue, cogs, operating_expenses, depreciation, amortization):
#     """
#     Базовая формула EBITDA:
#     EBITDA = Выручка - Себестоимость - Операционные расходы + Амортизация
#     """
#     ebitda = revenue - cogs - operating_expenses + depreciation + amortization
#     return ebitda

# Пример использования
# revenue = 1000000  # Выручка
# cogs = 600000      # Себестоимость продаж
# operating_expenses = 200000  # Операционные расходы
# depreciation = 50000         # Амортизация ОС
# amortization = 30000         # Амортизация НМА

# ebitda = calculate_ebitda_basic(revenue, cogs, operating_expenses, depreciation, amortization)
# print(f"EBITDA: {ebitda:,.2f}")  # EBITDA: 280,000.00

# ---------------------------------------
# Расчет через операционную прибыль (EBIT)

# def calculate_ebitda_from_ebit(ebit, depreciation, amortization):
#     """
#     EBITDA = EBIT + Амортизация ОС + Амортизация НМА
#     """
#     return ebit + depreciation + amortization

# Пример
# ebit = 200000  # Операционная прибыль
# depreciation = 50000
# amortization = 30000

# ebitda = calculate_ebitda_from_ebit(ebit, depreciation, amortization)
# print(f"EBITDA: {ebitda:,.2f}")

# # ------------------------------------------------
# # ООП подход с классом Company
# class Company:
#     def __init__(self, name, revenue, cogs, operating_expenses, depreciation, amortization):
#         self.name = name
#         self.revenue = revenue
#         self.cogs = cogs
#         self.operating_expenses = operating_expenses
#         self.depreciation = depreciation
#         self.amortization = amortization
    
#     @property
#     def ebit(self):
#         """Операционная прибыль (EBIT)"""
#         return self.revenue - self.cogs - self.operating_expenses
    
#     @property
#     def ebitda(self):
#         """EBITDA"""
#         return self.ebit + self.depreciation + self.amortization
    
#     def financial_report(self):
#         """Генерация финансового отчета"""
#         return f"""
# Финансовый отчет: {self.name}
# Выручка: {self.revenue:,.2f}
# Себестоимость: {self.cogs:,.2f}
# Операционные расходы: {self.operating_expenses:,.2f}
# EBIT: {self.ebit:,.2f}
# Амортизация ОС: {self.depreciation:,.2f}
# Амортизация НМА: {self.amortization:,.2f}
# EBITDA: {self.ebitda:,.2f}
# """

# Использование
# company = Company(
#     name="ТехноКорп",
#     revenue=1500000,
#     cogs=800000,
#     operating_expenses=300000,
#     depreciation=60000,
#     amortization=40000
# )

# print(company.financial_report())

# --------------------------------
# Работа с pandas для анализа нескольких компаний

# import pandas as pd
# import numpy as np

# def create_financial_dataset():
#     """Создание тестового датасета с финансовыми показателями"""
#     data = {
#         'company': ['Company_A', 'Company_B', 'Company_C', 'Company_D'],
#         'revenue': [1000000, 1500000, 800000, 1200000],
#         'cogs': [600000, 900000, 480000, 720000],
#         'operating_expenses': [200000, 300000, 160000, 240000],
#         'depreciation': [50000, 75000, 40000, 60000],
#         'amortization': [30000, 45000, 24000, 36000]
#     }
    # return pd.DataFrame(data)

# def calculate_ebitda_df(df):
#     """Расчет EBITDA для DataFrame"""
#     df = df.copy()
#     df['ebit'] = df['revenue'] - df['cogs'] - df['operating_expenses']
#     df['ebitda'] = df['ebit'] + df['depreciation'] + df['amortization']
#     df['ebitda_margin'] = (df['ebitda'] / df['revenue'] * 100).round(2)
#     return df

# Анализ нескольких компаний
# df = create_financial_dataset()
# df_analysis = calculate_ebitda_df(df)

# print("Финансовый анализ компаний:")
# print(df_analysis.to_string(index=False))

# Дополнительный анализ
# print(f"\nСредняя маржа EBITDA: {df_analysis['ebitda_margin'].mean():.2f}%")
# print(f"Лучшая маржа EBITDA: {df_analysis['ebitda_margin'].max():.2f}%")

# -------------------------------------
def ebitda_calculator():
    """Интерактивный калькулятор EBITDA"""
    print("Калькулятор EBITDA")
    print("Введите финансовые показатели:")
    
    try:
        net_income = float(input("Чистая прибыль: "))
        interest = float(input("Проценты по кредитам: "))
        taxes = float(input("Налоги: "))
        depreciation = float(input("Износ основных средств: "))
        amortization = float(input("Амортизация нематериальных активов: "))
        
        ebitda = net_income + interest + taxes + depreciation + amortization
        
        print(f"\nРезультат расчета:")
        print(f"EBITDA = {ebitda:,.2f} руб.")
        
    except ValueError:
        print("Ошибка! Вводите только числа.")

# Запуск калькулятора
ebitda_calculator()
# --------------------------
class InvestmentProject:
    def __init__(self, initial_investment, cash_flows):
        self.initial_investment = initial_investment
        self.cash_flows = cash_flows
        self.all_cash_flows = [initial_investment] + cash_flows
    
    def npv(self, rate):
        """Рассчитывает NPV для проекта"""
        return sum(cf / (1 + rate) ** i for i, cf in enumerate(self.all_cash_flows))
    
    def irr(self, guess=0.1, max_iter=1000, tolerance=1e-6):
        """Рассчитывает внутреннюю норму доходности (IRR)"""
        x = guess
        for i in range(max_iter):
            npv_value = self.npv(x)
            npv_derivative = sum(-i * cf / (1 + x) ** (i + 1) for i, cf in enumerate(self.all_cash_flows) if i > 0)
            
            if abs(npv_value) < tolerance:
                return x
            
            if abs(npv_derivative) < tolerance:
                break
                
            x = x - npv_value / npv_derivative
        
        return x

# Использование класса
project = InvestmentProject(initial_investment=-1000, cash_flows=[300, 400, 500, 200])

npv_result = project.npv(0.1)
irr_result = project.irr()

print(f"NPV при 10%: {npv_result:.2f}")
print(f"IRR проекта: {irr_result:.2%}")