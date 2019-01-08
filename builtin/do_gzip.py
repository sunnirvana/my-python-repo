#!/usr/bin/env python3
import shutil
import gzip


def gzip_file(src, dst):
    with open(src, 'rb') as f_in, gzip.open(dst, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)


def ungzip_file(src, dst):
    with gzip.open(src, 'rb') as f_in, open(dst, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

# vim: ts=4 sw=4 sts=4 expandtab
