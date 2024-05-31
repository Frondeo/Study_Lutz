from timeit import timeit

import dis

a_list = list(range(1_000_000))

# print(timeit("list[0]", "from __main__ import a_list"))
# print(timeit("list[500000]", "from __main__ import a_list"))
# print(timeit("list[-1]", "from __main__ import a_list"))
# print(id(a_list[1]))

print(timeit("list()"))
print(timeit("tuple()"))
