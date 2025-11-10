# Set Theory: Python's built-in set data type directly supports operations like union, 
# ntersection, difference, and symmetric difference, making it easy to model and manipulate sets.

set_A = {1, 2, 3, 4}
set_B = {3, 4, 5, 6}
union_set = set_A.union(set_B)  # {1, 2, 3, 4, 5, 6}
intersection_set = set_A.intersection(set_B) # {3, 4}