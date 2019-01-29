#!/usr/bin/env python3
import base64
import os
from .common import get_file_md5


def bin2b64c(binary):
    try:
        with open(binary, 'rb') as fp:
            data = fp.read()
            print('<bin2str>: data bin len: %s' % (len(data)))
            b64str = base64.b64encode(data)
            print('<bin2str>: data src len: %s' % (len(b64str)))
            print('head 6 bytes: %s, tail 6 bytes: %s', b64str[:6], b64str[-6:])
            return b64str
    except Exception as e:
        raise e


def b64c2bin_o(b64code):
    try:
        ori_data = bytes(str(b64code), encoding='utf-8')
        #  print('ori_data: ', ori_data)
        data = base64.b64decode(ori_data)
        return data
    except Exception as e:
        raise e


def b64c2bin_f(b64c_file):
    try:
        with open(b64c_file, 'rb') as fp:
            b64str = fp.read()
            # bug: 下面这行代码会导致b64str变化
            b64str = bytes(str(b64str), encoding='utf-8')
            print('<str2bin>: data str len: %s' % (len(b64str)))
            print('head 6 bytes: %s, tail 6 types: %s', b64str[:6], b64str[-6:])
            data = base64.b64decode(b64str)
            print('<str2bin>: data bin len: %s' % (len(data)))
            return data
    except Exception as e:
        raise e


def echo(process, file):
    print('%s, file: %s \n\t md5: %s' % (process, file, get_file_md5(file)))


if __name__ == '__main__':
    path = 'wks'

    file_bin = os.path.join(path, 'inst.wk')
    echo('bin', file_bin)

    file_bin_str = os.path.join(path, 'inst.wk.str')
    data = bin2b64c(file_bin)
    with open(file_bin_str, 'wb') as f:
        f.write(data)
    echo('bin -> str', file_bin_str)

    from .do_gzip import gzip_file, ungzip_file

    file_bin_str_gzip = os.path.join(path, 'inst.wk.str.gzip')
    gzip_file(file_bin_str, file_bin_str_gzip)
    echo('bin -> str -> gzip', file_bin_str_gzip)

    file_bin_str_gzip_ungzip = os.path.join(path, 'inst.wk.str.gzip.ungzip')
    ungzip_file(file_bin_str_gzip, file_bin_str_gzip_ungzip)
    echo('bin -> str -> gzip -> ungzip', file_bin_str_gzip_ungzip)

    file_bin_str_gzip_ungzip_bin = os.path.join(path, 'inst.wk.str.gzip.ungzip.bin')
    with open(file_bin_str_gzip_ungzip_bin, 'wb') as f:
        f.write(b64c2bin_f(file_bin_str_gzip_ungzip))
    echo('bin -> str -> gzip -> ungzip -> bin', file_bin_str_gzip_ungzip_bin)

    #  file_bin_str_bin1 = os.path.join(path, 'inst.str.bin1')
    #  with open(file_bin_str_bin1, 'wb') as f:
    #  f.write(b64c2bin_o(data))
    #  print('bin -> str -> bin file: %s \n\t md5: %s',
    #  file_bin_str_bin1, get_file_md5(file_bin_str_bin1))
