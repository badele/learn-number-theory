import os
import sys

# Add module path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import lib.math

# Search prime numbers
def a000040_prime_numbers(maxn):
  sieve = [True] * maxn
  for i in range(3,int(maxn**0.5)+1,2):
      if sieve[i]:
          sieve[i**2::2*i]=[False]*((maxn-i**2-1)//(2*i)+1)
  return [2] + [i for i in range(3,maxn,2) if sieve[i]]

# Search perfect numbers
def a000396_perfect_numbers(maxn):
  a000040_list = a000040_prime_numbers(maxn)
  for p in a000040_list:
    pn = 2**(p-1)*(2**p-1)
    divs = lib.math.divisors(pn)
    if pn == lib.math.sum_divisors(divs[0:-1]):
      yield pn
