import os
import sys
import argparse

# python3 A000396_perfect_numbers.py -n 30  57,09s user 0,03s system 99% cpu 57,411 total

# Add module path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Load math modules
import lib.math

MAXN=100

# Argument options
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--maxn",	type=int,help="(default: %(default)s)",default=MAXN)
ap.add_argument("-m", "--method",	choices=['fast', 'learn'],help="(default: %(default)s)",default='fast')
ap.add_argument("-b", "--bench", help="Active Bench",action='store_true')
ap.add_argument("-s", "--show-sequence", help="Show sequence number",action='store_true')
args = vars(ap.parse_args())

# Import function method
if args['method'] == 'fast':
  from lib.oeis.fast import a001348_mersenne_number
else:
  from lib.oeis.learn import a001348_mersenne_number

# Compute primes
a001348_list = list(a001348_mersenne_number(args['maxn']))
if not args['bench']:
    for n,p in enumerate(a001348_list,1):
        if args['show_sequence']:
            print(f'{n} {p}')
        else:
            print(p)
