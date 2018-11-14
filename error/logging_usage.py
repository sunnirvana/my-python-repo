import logging


def foo(s):
    _s = int(s)
    if _s == 0:
        raise ZeroDivisionError
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    # logger = logging.getLogger(__name__)
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)
        # print(e)


main()
print('END')
