set_A = {1, 2, 3, 4}
set_B = {3, 4, 5, 6}
union_set = set_A.union(set_B)  # {1, 2, 3, 4, 5, 6}
intersection_set = set_A.intersection(set_B) # {3, 4}


# ----------------------------

import itertools
    perms = list(itertools.permutations([1, 2, 3])) # [(1, 2, 3), (1, 3, 2), ...]
    combs = list(itertools.combinations([1, 2, 3, 4], 2)) # [(1, 2), (1, 3), ...]
