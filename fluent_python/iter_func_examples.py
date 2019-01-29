import itertools
import operator


def print_res(meta, res):
    print('*' * 50)
    print('meta: ', meta)
    for code in res:
        print('code: ', code)
        print('result: ', eval(code))


# 用于过滤的生成器函数
def vowel(c: str):
    return c.lower() in 'aeiou'


text = 'Aardvark'
codes1 = [
    'list(filter(vowel, text))',
    'list(itertools.filterfalse(vowel, text))',
    'list(itertools.dropwhile(vowel, text))',
    'list(itertools.takewhile(vowel, text))',
    'list(itertools.compress(text, (1, 0, 1, 1, 0, 1)))',
    'list(itertools.islice(text, 4))',
    'list(itertools.islice(text, 4, 7))',
    'list(itertools.islice(text, 1, 7, 2))',
]
print_res(text, codes1)

# 用于映射的生成器函数
sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]
codes2 = [
    'list(itertools.accumulate(sample))',
    'list(itertools.accumulate(sample, min))',
    'list(itertools.accumulate(sample, max))',
    'list(itertools.accumulate(sample, operator.mul))',
    'list(itertools.accumulate(range(1,11), operator.mul))',
    'list(enumerate("albatroz", 1))',
    'list(map(operator.mul, range(11), [2, 4, 8]))',
    'list(itertools.starmap(operator.mul, enumerate("albatroz", 1)))',
    'list(itertools.starmap(lambda a, b: b / a, enumerate(itertools.accumulate(sample), 1)))'
]
print_res(sample, codes2)

# 用于合并的生成器函数
codes3 = [
    "list(itertools.chain('ABC', range(2)))",
    "list(itertools.chain(enumerate('ABC')))",
    "list(itertools.chain.from_iterable(enumerate('ABC')))",
    "list(zip('ABC', range(5)))",
    "list(zip('ABC', range(5), [10, 20, 30, 40]))",
    "list(itertools.zip_longest('ABC', range(5)))",
    "list(itertools.zip_longest('ABC', range(5), fillvalue='?'))"
]
print_res('', codes3)

# itertools.product
codes4 = [
    "list(itertools.product('ABC', range(2)))",
    "list(itertools.product('AK', 'spades hearts diamonds clubs'.split()))",
    "list(itertools.product('ABC'))",
    "list(itertools.product('ABC', repeat=2))",
    "list(itertools.product('ABC', 'ABC'))",
    "list(itertools.product(range(2), repeat=3))",
    "list(itertools.product(range(2), range(2), range(2)))"
]
print_res('', codes4)
rows = itertools.product('AB', range(2), repeat=2)
print("itertools.product('AB', range(2), repeat=2)")
for row in rows:
    print(row)

# 把输入的各个元素扩展成多个输出元素的生成器函数
# count, repeat, cycle
print("*"*50)
ct = itertools.count()
for i in range(4):
    print(next(ct))

print(list(itertools.islice(itertools.count(1, .3), 3)))

cy = itertools.cycle('ABC')
print(next(cy))

print(list(itertools.islice(cy, 7)))
rp = itertools.repeat(7)
print(next(rp), next(rp))
print(list(itertools.repeat(8, 4)))
print(list(map(operator.mul, range(11), itertools.repeat(5))))

# 组合学生成器函数会从输入的各个元素中产生多个值
print(list(itertools.combinations('ABC', 2)))
print(list(itertools.combinations_with_replacement('ABC', 2)))
print(list(itertools.permutations('ABC', 2)))
print(list(itertools.product('ABC', repeat=2)))
