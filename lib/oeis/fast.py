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


def a000040_prime_numbers_boolean(maxn):
    # Try load primes range from cache
    primes = lib.cache.load_from_bitarray(f'a000040_primes_{maxn}_boolean')
    if primes is not None:
        return primes

    # Generate primes
    isprime = bitarray(maxn)
    isprime.setall('1')
    for i in range(3, int(maxn**0.5) + 1, 2):
        if isprime[i]:
            isprime[i**2::2 * i] = False

    # Set no prime numbers
    isprime[0:2] = False
    isprime[4::2] = False

    # Save primes to cache
    lib.cache.save_from_bitarray(isprime, f'a000040_primes_{maxn}_boolean')

    return isprime


# https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
def a000040_prime_numbers(maxn):
    assert maxn >= 6

    primes = lib.cache.numpy_load(f'a000040_primes_{maxn}')
    if primes is not None:
        return primes

    sieve = np.ones(maxn // 3 + (maxn % 6 == 2), dtype=np.bool)
    sieve[0] = False
    for i in range(int(maxn**0.5) // 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[((k * k) // 3)::2 * k] = False
            sieve[(k * k + 4 * k - 2 * k * (i & 1)) // 3::2 * k] = False

    # Save primes to cache
    primes = np.r_[2, 3, ((3 * np.nonzero(sieve)[0] + 1) | 1)]
    lib.cache.numpy_save(primes, f'a000040_primes_{maxn}')

    return primes


def a001348_mersenne_number(maxn):
    # Try load primes range from cache
    mersenne = lib.cache.load_cache(f'a001348_mersenne_primes_{maxn}')
    if mersenne is not None:
        return mersenne

    isprimes = a000040_prime_numbers_boolean(maxn)

    mersenne = []
    for p in range(len(isprimes)):
        if isprimes[p]:
            m = 2**p - 1
            if m > maxn:
                break

            if isprimes[m]:
                mersenne.append(m)

    # Save primes to cache
    lib.cache.save_cache(mersenne, f'a001348_mersenne_primes_{maxn}')

    return mersenne


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
