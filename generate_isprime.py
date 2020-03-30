import os
import sys
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
ap.add_argument("-i", "--in", type=str,
                help="load file: %(default)s)", default="/tmp/numbers.npy")
ap.add_argument("-o", "--out", type=str,
                help="save file: %(default)s)", default="/tmp/isprimes.npy")
args = vars(ap.parse_args())

from sympy import divisors, isprime


def zero_runs(a):  # from link
    iszero = np.concatenate(([0], np.equal(a, 0).view(np.int8), [0]))
    print(iszero)
    absdiff = np.abs(np.diff(iszero))
    ranges = np.where(absdiff == 1)[0].reshape(-1, 2)
    return ranges


# Load numbers
numbers = np.load(args['in'])

# Compute isprime
isprimes = []
for n in numbers:
    n = int(n)
    isprimes.append(isprime(n))

isprimes = np.array(isprimes).astype(int)

np.save(args['out'], isprimes)
