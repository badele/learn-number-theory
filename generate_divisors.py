#!/bin/python

# time python generate_divisors.py -n 1000000  22,57s user 0,17s system 99% cpu 22,807 total
import os
import sys
import argparse

# Load math modules
import lib.math
import lib.cache

MAXN=100

# Argument options
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--maxn",	type=int,help="(default: %(default)s)",default=MAXN)
args = vars(ap.parse_args())

maxn = args['maxn']

divs = [[1]] * (maxn+1)
for n in range(2,maxn+1):
    for d in range(n,maxn+1,n):
        curdiv = list(divs[d])
        curdiv.append(n)
        divs[d] = curdiv
divs[0] = []
