def is_odd(n):
    return n % 2 == 1


L = list(filter(is_odd, range(1, 20)))
L1 = list(filter(lambda n: n % 2 == 1, range(1, 20)))

print(L, L1, L == L1, sep='\n')
