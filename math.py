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

