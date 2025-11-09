# Set Theory: Python's built-in set data type directly supports operations like union, 
# ntersection, difference, and symmetric difference, making it easy to model and manipulate sets.

set_A = {1, 2, 3, 4}
set_B = {3, 4, 5, 6}
union_set = set_A.union(set_B)  # {1, 2, 3, 4, 5, 6}
intersection_set = set_A.intersection(set_B) # {3, 4}

# ----------------------------
# Combinatorics: The itertools module provides functions like permutations, 
# combinations, and product for generating and analyzing combinatorial objects.

import itertools
    perms = list(itertools.permutations([1, 2, 3])) # [(1, 2, 3), (1, 3, 2), ...]
    combs = list(itertools.combinations([1, 2, 3, 4], 2)) # [(1, 2), (1, 3), ...]

# ----------------------------
# Graph Theory: Libraries like NetworkX offer extensive functionalities for creating,
# manipulating, and analyzing graphs, including algorithms for shortest paths, connectivity, and centrality measures.
