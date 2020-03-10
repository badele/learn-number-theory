import os
import sys
import argparse

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
  from lib.oeis.fast import a000040_prime_boolean_numbers
else:
  from lib.oeis.learn import a000040_prime_boolean_numbers

# Compute primes
a000040_list = list(a000040_prime_boolean_numbers(args['maxn']))
if not args['bench']:
  for n,p in enumerate(a000040_list,1):
    if args['show_sequence']:
      print(f'{n} {p}')
    else:
      print(p)
