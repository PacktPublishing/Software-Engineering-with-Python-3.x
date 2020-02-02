def get_fact_arr(n):
    fact = 1
    fact_list = []
    for x in range(n):
        fact = fact * x
        fact_list.append(fact)
    return fact_list

import timeit
print(timeit.timeit('x=get_fact_arr(100)',
             setup="from __main__ import get_fact_arr",
             number=5))