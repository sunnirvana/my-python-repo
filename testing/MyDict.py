
class MyDict(dict):
    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, k):
        try:
            return self[k]
        except KeyError:
            raise AttributeError(r"'MyDict' object has no attribute %s" % k)

    def __setattr__(self, k, v):
        self[k] = v


def main():
    mydict = MyDict(a=1, b=2)
    mydict.c = 'c'
    print(mydict)


if __name__ == '__main__':
    main()
