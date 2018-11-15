
"""[summary]

Raises:
    测试logging用法
    import logging
    logging.warn/debug/info/error.
    debug < info < warning < error, 选择info, 则不显示debug信息; 如果选择warning, 则不显示debug和info的信息

Returns:
    [type] -- [description]
"""
import logging

log_setting = {
    'filename': './error/log.txt',
    'filemode': 'w',
    'level': logging.WARNING,
}
logging.basicConfig(**log_setting)


def foo(s):
    _s = int(s)
    if _s == 0:
        raise ZeroDivisionError
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    # logger = logging.getLogger(__name__)
    logging.debug('I am debug')
    logging.info('I am info')
    logging.warn('I am warning')
    logging.error('I am error')

    try:
        bar('0')
    except Exception as e:
        logging.exception(e)
        # print(e)


main()
print('END')
