#!/bin/python

# time python3 generate_primes.py -n 100000000  8,65s user 0,70s system 99% cpu 9,381 total

import os
import sys
import argparse

import numpy as np
from sympy import isprime

MAXN = 10000

# Argument options
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--maxn", type=int,
                help="(default: %(default)s)", default=MAXN)
ap.add_argument("-o", "--out", type=str,
                help="save to filename: %(default)s)", default="/tmp/primes_euler.npy")
ap.add_argument("-p", "--prime",
                help="Only prime: : %(default)s)", action="store_true", default=False)
args = vars(ap.parse_args())

maxn = args['maxn']

eulers = []
for n in range(1, maxn):
    eulern = n**2 + n + 41

    if args['prime']:
        if isprime(eulern):
            eulers.append(eulern)
    else:
        eulers.append(eulern)

arr = np.array(eulers)
np.save(args['out'], arr)
