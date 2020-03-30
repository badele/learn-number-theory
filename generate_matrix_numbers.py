import os
import sys
import math
import argparse
import numpy as np
from bitarray import bitarray
# Add module path
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")))

# Load math modules
import lib.math

MAXN = 100

# Argument options
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--maxn", type=int,
                help="(default: %(default)s)", default=MAXN)
ap.add_argument("-m", "--method",
                choices=['fast', 'learn'], help="(default: %(default)s)", default='fast')
ap.add_argument("-b", "--bench", help="Active Bench", action='store_true')
ap.add_argument("-s", "--show-sequence",
                help="Show sequence number", action='store_true')
args = vars(ap.parse_args())

from itertools import permutations


from lib.oeis.fast import a000040_prime_numbers, a000040_prime_numbers_boolean

PRANGE = 100000000
PSEARCH = 1000
# isprimes = a000040_prime_numbers_boolean(PRANGE)

from sympy import divisors, isprime


maxn = args['maxn']

nblines = math.ceil((maxn + 1) / 10)
numbers = np.arange(0, 10 * nblines)
numbers = numbers.reshape(nblines, 10)

maxlen = len(str(maxn))

for x in range(0, nblines):
    for y in range(0, 10):
        print(f'{numbers[x,y]:{maxlen}d},', end='')
    print()
