#!/usr/bin/env python3

import numpy as np
from numba import jit

nobs = 10000


def proc_numpy(x, y, z):
    x = x*2 - (y * 55)
    y = x + y*2
    z = x + y + 99
    z = z * (z - .88)


@jit
def proc_numba(xx, yy, zz):
    for j in range(nobs):
        x, y = xx[j], yy[j]

        x = x*2 - (y * 55)
        y = x + y*2
        z = x + y + 99
        z = z * (z - .88)

        zz[j] = z
    return zz


x = np.random.randn(nobs)
y = np.random.randn(nobs)
z = np.zeros(nobs)

res_numpy = proc_numpy(x, y, z)

z = np.zeros(nobs)
res_numba = proc_numba(x, y, z)

# vim: ts=4 sw=4 sts=4 expandtab
