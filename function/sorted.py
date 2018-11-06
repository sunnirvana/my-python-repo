'https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318230588782cac105d0d8a40c6b450a232748dc854000'
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return str.lower(t[0])


def by_score(t):
    return t[1]


L2 = sorted(L, key=by_name)
L3 = sorted(L, key=by_score)
L2_r = sorted(L, key=by_name, reverse=True)
L3_r = sorted(L, key=by_score, reverse=True)
print(L2, L2_r, L3, L3_r, sep='\n')
