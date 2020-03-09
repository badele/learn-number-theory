import os
import sys

# Add module path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import lib.math

# Search prime numbers
def a000040_prime_numbers(maxn):
     for n in range(2,maxn+1):
         divisors = lib.math.divisors(n)
         if len(divisors)==2:
            yield n
