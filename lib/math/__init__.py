import os
import sys
from sympy.ntheory import primefactors, factorint, isprime

# Add module path
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")))

import lib.cache


def sqrt(n):
    # Compute root square https://oeis.org/A000290
    return n**.5


def divisors(n):
    # Search divisors
    if n == 0:
        return []

    divisors = [1]
    factors = factorint(n).items()
    for f, r in list(factors):
        divisors.extend([f] * r)

    return divisors


def sum_divisors(divs):
    # Sum digit number ex: 123 = 6
    s = 0
    for d in divs:
        s += d

    return s


def get_divisors_list(maxn):
    # Return computed list for some numbers
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
