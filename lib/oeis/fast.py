import os
import sys
import numpy as np
from bitarray import bitarray

# Add module path
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../..")))

import lib.math


# def fastrange(start, stop, step):
#     idx = start
#     while idx < stop:
#         yield idx
#         idx += step

# Search prime numbers
# https://stackoverflow.com/a/3035188/2015612


# Search perfect numbers
def a000396_perfect_numbers(maxn):
    a000040_list = a000040_prime_numbers(maxn)
    for p in a000040_list:
        pn = 2**(p - 1) * (2**p - 1)
        divs = lib.math.divisors(pn)
        if pn == lib.math.sum_divisors(divs[0:-1]):
            yield pn


def a000290_perfect_squares_boolean(maxn):
    isquares = bitarray(maxn)
    isquares.setall(False)

    idx = 1
    square = 1
    while square < maxn:
        isquares[square] = True
        idx += 1
        square = idx**2

    pfilename = '/tmp/result'
    with open(pfilename, 'wb') as f:
        isquares.tofile(f)

    return isquares


def a000290_squares(maxn):
    squares = lib.cache.load_from_bitarray(f'a000290_squares{maxn}')
    if squares is not None:
        return squares

    squares = {}
    idx = 1
    square = 1
    while square < maxn:
        squares[square] = idx
        idx += 1
        square = idx**2

    lib.cache.save_cache(squares, f'a000290_squares{maxn}')

    return squares
