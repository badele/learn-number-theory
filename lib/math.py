import os
import sys

# Add module path
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")))

import lib.cache

# Compute root square https://oeis.org/A000290


def sqrt(n):
    return n**.5

# Search divisors


def divisors(n):
    if n < 1:
        return []

    divs = [1]
    for i in range(2, int(sqrt(n)) + 1):
        if i != n and n % i == 0:
            divs.extend([i, int(n / i)])
    divs.extend([n])
    return sorted(list(set(divs)))

# Sum divisors


def sum_divisors(divs):
    s = 0
    for d in divs:
        s += d

    return s

# Sum digit number ex: 123 = 6


def sum_digit_number(num):
    sdigit = 0
    for s in str(num):
        sdigit += int(s)

    return sdigit

# Return computed list for some numbers


def get_divisors_list(maxn):
    divs = lib.cache.load_cache(f'divs_{maxn}')
    if divs is not None:
        return divs

    divs = [[1]] * (maxn + 1)
    for n in range(2, maxn + 1):
        for d in range(n, maxn + 1, n):
            curdiv = list(divs[d])
            curdiv.append(n)
            divs[d] = curdiv
    divs[0] = []
    lib.cache.save_cache(divs, f'divs_{maxn}')

    return divs
