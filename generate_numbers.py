#!/bin/python

# time python3 generate_primes.py -n 100000000  8,65s user 0,70s system 99% cpu 9,381 total

import os
import sys
import argparse
import numpy as np


# Argument options
ap = argparse.ArgumentParser()
ap.add_argument("-o", "--out", type=str,
                help="out to filename: %(default)s)", default="/tmp/numbers.npy")
ap.add_argument("-s", "--start", type=int,
                help="(START: %(default)s)", default=0)
ap.add_argument("-e", "--end", type=int,
                help="(END: %(default)s)", default=1000)
args = vars(ap.parse_args())


n = np.arange(args['start'], args['end'] + 1, dtype=int)
np.save(args['out'], n)
