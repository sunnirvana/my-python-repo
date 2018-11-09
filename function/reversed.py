class FloatRange:
    def __init__(self, start, end, step):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        t = self.start
        while t <= self.end:
            yield t
            t += self.step

    def __reversed__(self):
        t = self.end
        while t >= self.start:
            yield t
            t -= self.step


for x in FloatRange(10, 12, 0.2):
    print(x)

for _x in reversed(FloatRange(10, 12, 0.2)):
    print(_x)
