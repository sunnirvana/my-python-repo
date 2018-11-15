"""[summary]
    试用assert
Returns:
    [type] -- [description]
"""


def foo(s):
    print('in foo')
    n = int(s)
    # 如果不满足assert的条件, 则返回AssertionError, 中断程序
    assert n > 10, "n shall be more than 10!!!"
    return n


def main():
    foo('100')
    foo('0')


if __name__ == '__main__':
    main()
