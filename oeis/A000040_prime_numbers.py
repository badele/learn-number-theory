
MAXN=100

import os
import sys

# Add module path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Load math modules
import lib.math
import lib.oeis

# Compute primes
a000040_list = lib.oeis.a000040_prime_numbers(MAXN)
for n,p in enumerate(a000040_list,1):
  print(f'{n} {p}')
