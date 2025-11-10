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



