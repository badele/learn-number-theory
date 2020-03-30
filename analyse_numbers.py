#!/bin/python

import sys
import json
import argparse
import sympy as sp
import numpy as np
import pandas as pd
from tabulate import tabulate
import matplotlib.pylab as plt

import lib.math
import lib.digit

# num
# prime     A000040 - primes numbers
# sprime    A001358 - semi prime - two primes divisors (also same prime divisors)
# aprime    A006562 - middle prime
# dprime    Only prime divisors
# fp2       A000290 - Perfect Square
# fp3       A000578 - Perfect Cube
# db3       A001703 - Divisible by 3
# divisors  all divisors
# nb_div    nb divisors
# nb_divo   odd nb divisors
# ddigit    distinct digit list
# ndigit    nb distinct digit list
# fdigit    First digit
# ldigit    Last digit
# dgsum     sum digit number ex: 147 = 12
# dr        A010888 - digit root(sum digit) ex: 147 = 3
# sdiv      sum of divisors
# pnumber   A000396 - perfect number = n == (sdiv - n)
# ppdist    A001223 - prime gasp
# npdist    A001223 - prime gasp

# atwins    A014574 - average of twins prime number
# erdigit   A271569 - infinite sum same digit = digit

# Argument options
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--in", type=str,
                help="load number from filename", default="/tmp/numbers.npy")
ap.add_argument("-o", "--out", type=str,
                help="output number to filename", default="/tmp/numbers_info.csv")
args = vars(ap.parse_args())

# Set pandas options
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# Init vars
numlist = []
lastprime = 2

numbers = np.load(args['in'])

snumbers = pd.Series(numbers, name='num')
df = pd.DataFrame(snumbers)

idx = pd.Series(np.arange(1, len(numbers) + 1, dtype=int))
df['idx'] = idx
df['pidx'] = np.nan
df['nidx'] = np.nan

# divisors
df['divs'] = df['num'].apply(lib.math.divisors)
df['nb_divs'] = df['divs'].apply(lambda n: len(n))

# Prime
df['prime'] = df['nb_divs'] == 2
isprime = df['prime'] == 1
df.loc[isprime, 'npdist'] = df[isprime]['num'].shift(-1) - df[isprime]['num']
df.loc[isprime, 'ppdist'] = df[isprime]['npdist'].shift(1)
df.loc[isprime, 'aprime'] = df[isprime]['ppdist'] == df[isprime]['npdist']
df.loc[isprime, 'nidx'] = df[isprime]['idx'].shift(-1) - df[isprime]['idx']
df.loc[isprime, 'pidx'] = df[isprime]['nidx'].shift(1)

# Sum digit number
df['dgsum'] = df['num'].apply(lambda n: lib.digit.dsum(n))
# Infinite sum digit number
df['dr'] = df['num'].apply(lambda n: lib.digit.digital_root(n))

df['dgsumb3'] = df['dgsum'] % 3 == 0
df['dgsumb9'] = df['dgsum'] % 9 == 0

# Divisible by x
df['d2'] = df['num'] % 2 == 0
df['d3'] = df['num'] % 3 == 0
df['d5'] = df['num'] % 5 == 0
df['d7'] = df['num'] % 7 == 0
df['d11'] = df['num'] % 11 == 0

# Perfect square
roundedsquare = round(df['num'] ** .5)
isperfectsquare = roundedsquare**2 == df['num']
df.loc[isperfectsquare, 'fp2'] = df[isperfectsquare]['num'] ** .5

# Perfect cube
roundedcube = round(df['num'] ** (1 / 3))
isperfectscube = roundedcube**3 == df['num']
df.loc[isperfectscube, 'fp3'] = df[isperfectscube]['num'] ** (1 / 3)


# Convert to string
df['strnum'] = df['num'].astype(str)

# Number digits
df['ndigit'] = df['strnum'].apply(lambda n: len(n))

# Distinct digits
df['ddigit'] = df['strnum'].apply(lambda n: sorted(list(map(int, set(n)))))

# Number distinct digit
df['nddigit'] = df['ddigit'].apply(lambda n: len(n))

# First digit
df['fdigit'] = df['strnum'].apply(lambda n: n[0])

# Last digit
df['ldigit'] = df['strnum'].apply(lambda n: n[-1])

# Same Fist and last digit
df['lfedigit'] = df['fdigit'] == df['ldigit']


count = df.groupby('dr').count()
df.to_csv(args['out'])
