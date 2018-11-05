def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


for expr in ['gcd(0, 1)', 'gcd(1, 0)', 'gcd(1024, 2048)', 'gcd(1024, 2000)']:
    print('{:<6}'.format(expr))
    result = eval(expr)
    print(' result of {}: {}'.format(expr, result))
