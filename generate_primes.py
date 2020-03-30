#!/bin/python

# time python3 generate_primes.py -n 100000000  8,65s user 0,70s system 99% cpu 9,381 total

import os
import sys
import argparse

# Load math modules
import numpy as np
from lib.math.prime import a000040_prime_numbers

MAXN = 100000000

# Argument options
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--maxn", type=int,
                help="(default: %(default)s)", default=MAXN)
ap.add_argument("-o", "--out", type=str,
                help="save to filename: %(default)s)", default="/tmp/primes.npy")
args = vars(ap.parse_args())

primes = a000040_prime_numbers(args['maxn'])

primes = np.array(primes)
np.save(args['out'], primes)
