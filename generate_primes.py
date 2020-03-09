#!/bin/python

# time python3 generate_primes.py -n 100000000  8,65s user 0,70s system 99% cpu 9,381 total

import os
import sys
import argparse

# Load math modules
import lib.math
from lib.oeis.fast import a000040_prime_numbers
import lib.cache

MAXN=100000000

# Argument options
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--maxn",	type=int,help="(default: %(default)s)",default=MAXN)
args = vars(ap.parse_args())

primes = a000040_prime_numbers(args['maxn'])
