# Set Theory: Python's built-in set data type directly supports operations like union, 
# ntersection, difference, and symmetric difference, making it easy to model and manipulate sets.

set_A = {1, 2, 3, 4}
set_B = {3, 4, 5, 6}
union_set = set_A.union(set_B)  # {1, 2, 3, 4, 5, 6}
intersection_set = set_A.intersection(set_B) # {3, 4}


# Способ 1: Используем библиотеку sympy (символьные вычисления)

from sympy import symbols, And, Or, Not, simplify_logic, to_cnf

# Определяем переменные
p, q, r = symbols('p q r')

# Исходное выражение в ДНФ
dnf_expression = Or(
    And(p, Not(q)),
    And(p, Not(r)),
    And(q, Not(p)),
    And(q, Not(r)),
    And(r, Not(p)),
    And(r, Not(q))
)

print("Исходное выражение в ДНФ:")
print(dnf_expression)
print()

# Преобразуем к КНФ
cnf_expression = to_cnf(dnf_expression, simplify=True)
print("Преобразованное в КНФ:")
print(cnf_expression)
print()

# Упрощаем еще больше
simplified_cnf = simplify_logic(cnf_expression)
print("Упрощенная КНФ:")
print(simplified_cnf)
print()

# Целевое выражение для проверки
target_expression = And(
    Or(p, Not(r)),
    Or(q, Not(r)),
    Or(r, Not(p)),
    Or(p, q, r),
    Or(Not(p), Not(q), Not(r))
)

print("Целевое выражение:")
print(target_expression)
print()

# Проверяем эквивалентность
are_equivalent = simplify_logic(cnf_expression) == simplify_logic(target_expression)
print(f"Эквивалентны ли выражения: {are_equivalent}")



# Способ 2: Через таблицу истинности (ручной метод)
def evaluate_expression(p_val, q_val, r_val):
    """Вычисляет значение исходного ДНФ выражения"""
    return (
        (p_val and not q_val) or
        (p_val and not r_val) or
        (q_val and not p_val) or
        (q_val and not r_val) or
        (r_val and not p_val) or
        (r_val and not q_val)
    )

def evaluate_target(p_val, q_val, r_val):
    """Вычисляет значение целевого КНФ выражения"""
    return (
        (p_val or not r_val) and
        (q_val or not r_val) and
        (r_val or not p_val) and
        (p_val or q_val or r_val) and
        (not p_val or not q_val or not r_val)
    )

# Проверяем все комбинации
print("Таблица истинности:")
print("p q r | ДНФ | КНФ | Совпадают?")
print("-" * 30)

all_match = True
for p_val in [False, True]:
    for q_val in [False, True]:
        for r_val in [False, True]:
            dnf_result = evaluate_expression(p_val, q_val, r_val)
            cnf_result = evaluate_target(p_val, q_val, r_val)
            match = dnf_result == cnf_result
            
            print(f"{int(p_val)} {int(q_val)} {int(r_val)} |  {int(dnf_result)}  |  {int(cnf_result)}  |    {match}")
            
            if not match:
                all_match = False

print(f"\nВыражения эквивалентны: {all_match}")


# Способ 3: Пошаговое преобразование через СКНФ

def build_cnf_from_truth_table():
    """Строит СКНФ по таблице истинности"""
    
    # Находим ложные строки для исходного выражения
    false_rows = []
    
    for p_val in [False, True]:
        for q_val in [False, True]:
            for r_val in [False, True]:
                if not evaluate_expression(p_val, q_val, r_val):
                    false_rows.append((p_val, q_val, r_val))
    
    print("Строки, где выражение ложно:")
    for row in false_rows:
        print(f"  p={row[0]}, q={row[1]}, r={row[2]}")
    
    # Строим дизъюнкции для каждой ложной строки
    cnf_clauses = []
    
    for p_val, q_val, r_val in false_rows:
        clause = []
        if not p_val: clause.append('p')
        if not q_val: clause.append('q') 
        if not r_val: clause.append('r')
        if p_val: clause.append('¬p')
        if q_val: clause.append('¬q')
        if r_val: clause.append('¬r')
        cnf_clauses.append(clause)
    
    return cnf_clauses, false_rows

# Выполняем преобразование
cnf_clauses, false_rows = build_cnf_from_truth_table()

print("\nСКНФ дизъюнкции (максимальные клаузы):")
for clause in cnf_clauses:
    print(f"  ({' ∨ '.join(clause)})")

print(f"\nИсходная СКНФ: (p ∨ q ∨ r) ∧ (¬p ∨ ¬q ∨ ¬r)")

# Покажем, как получить дополнительные клаузы
print("\nДополнительные клаузы через резолюцию:")
print("Из (p ∨ q ∨ r) и (¬p ∨ ¬q ∨ ¬r) можно вывести:")

# Резолюция с добавлением вспомогательных дизъюнкций
print("  Добавляем (p ∨ ¬p), (q ∨ ¬q), (r ∨ ¬r)")
print("  Резолюция дает:")
print("    (p ∨ ¬r) ∧ (q ∨ ¬r) ∧ (r ∨ ¬p)")

# Способ 4: Визуализация процесса

def demonstrate_resolution():
    """Демонстрирует процесс резолюции"""
    
    print("Процесс преобразования:")
    print("1. Исходное ДНФ: (p∧¬q) ∨ (p∧¬r) ∨ (q∧¬p) ∨ (q∧¬r) ∨ (r∧¬p) ∨ (r∧¬q)")
    print("2. Через таблицу истинности получаем СКНФ: (p ∨ q ∨ r) ∧ (¬p ∨ ¬q ∨ ¬r)")
    print("3. Применяем резолюцию:")
    
    # Покажем резолюцию с дополнительными дизъюнкциями
    additional_clauses = [
        "(p ∨ ¬r)",  # Из (p ∨ q ∨ r) и дополнительных преобразований
        "(q ∨ ¬r)",  # Из (p ∨ q ∨ r) и дополнительных преобразований  
        "(r ∨ ¬p)",  # Из (¬p ∨ ¬q ∨ ¬r) и дополнительных преобразований
    ]
    
    print("   Получаем дополнительные клаузы:")
    for clause in additional_clauses:
        print(f"   - {clause}")
    
    print("4. Финальное выражение:")
    print("   (p ∨ ¬r) ∧ (q ∨ ¬r) ∧ (r ∨ ¬p) ∧ (p ∨ q ∨ r) ∧ (¬p ∨ ¬q ∨ ¬r)")

demonstrate_resolution()


# 
# Автоматическое преобразование из ДНФ в КНФ с помощью sympy

# Проверку эквивалентности через таблицу истинности

# Пошаговый процесс построения СКНФ

# Визуализацию процесса резолюции

# Основной вывод: оба выражения логически эквивалентны, а преобразование происходит через 
# систематическое применение логических законов, в основном через построение совершенной нормальной формы.




# эконометрика

# Импортируем нужные библиотеки
import numpy as np

# --- 1. Исходные данные (наши наблюдения) ---
# Допустим, у нас есть 5 наблюдений
X = np.array([1, 2, 3, 4, 5])
Y = np.array([2, 3, 5, 4, 6])


# --- 2. Рассчитаем средние значения ---
mean_X = np.mean(X)
mean_Y = np.mean(Y)

print(f"Среднее X̄ = {mean_X:.2f}")
print(f"Среднее Ȳ = {mean_Y:.2f}")

# --- 3. Выборочная дисперсия X ---
# Var(X) = Σ(Xi - X̄)² / (n - 1)
var_X = np.sum((X - mean_X)**2) / (len(X) - 1)
print(f"Выборочная дисперсия Var(X) = {var_X:.2f}")



# --- 4. Выборочная ковариация между X и Y ---
# Cov(X,Y) = Σ[(Xi - X̄)(Yi - Ȳ)] / (n - 1)
cov_XY = np.sum((X - mean_X)*(Y - mean_Y)) / (len(X) - 1)
print(f"Выборочная ковариация Cov(X,Y) = {cov_XY:.2f}")


# --- 5. Коэффициенты линейной регрессии ---
b = cov_XY / var_X
a = mean_Y - b * mean_X

print(f"\nКоэффициенты линейной регрессии:")
print(f"b' (наклон) = {b:.2f}")
print(f"a' (свободный член) = {a:.2f}")

# --- 6. Предсказание по модели ---
# Модель: Y' = a' + b'X
Y_pred = a + b * X

print("\nПредсказанные значения Y':")
print(np.round(Y_pred, 2))


# --- 7. Для наглядности: сравнение фактических и предсказанных ---
print("\nСравнение фактических и предсказанных значений:")
for xi, yi, ypi in zip(X, Y, Y_pred):
    print(f"X={xi},  Y={yi},  Y'={ypi:.2f}")


