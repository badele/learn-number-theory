import os
import sys

# Add module path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import lib.math


# Search prime numbers
def a000040_prime_numbers(maxn):
  # Try load primes range from cache
  primes = lib.cache.load_cache(f'primes_{maxn}')
  if primes is not None:
    return primes

  # Generate primes
  sieve = [True] * maxn
  for i in range(3,int(maxn**0.5)+1,2):
      if sieve[i]:
          sieve[i**2::2*i]=[False]*((maxn-i**2-1)//(2*i)+1)

  # Save primes to cache
  primes = [2] + [i for i in range(3,maxn,2) if sieve[i]]
  lib.cache.save_cache(primes,f'primes_{maxn}')

  return primes

def a001348_mersenne_number(maxn):
  # Try load primes range from cache
  mersenne = lib.cache.load_cache(f'mersenne_primes_{maxn}')
  if mersenne is not None:
    return mersenne

  primes = a000040_prime_numbers(maxn)
  isprimes = lib.math.value_in_idx(maxn, primes)

  mersenne = []
  for n in range(2,maxn+1):
    m = 2**n-1
    if m > maxn:
      mersenne.append(-1)
      continue
    if isprimes[m]:
      mersenne.append(m)

  # Save primes to cache
  lib.cache.save_cache(mersenne,f'mersenne_primes_{maxn}')

  return mersenne


# Search perfect numbers
def a000396_perfect_numbers(maxn):
  a000040_list = a000040_prime_numbers(maxn)
  for p in a000040_list:
    pn = 2**(p-1)*(2**p-1)
    divs = lib.math.divisors(pn)
    if pn == lib.math.sum_divisors(divs[0:-1]):
      yield pn

# # Search perfect numbers
# def a000396_perfect_numbers(maxn):
#   a000040_list = lib.math.get_divisors_list(maxn)
#   for p in a000040_list:
#     pn = 2**(p-1)*(2**p-1)
#     divs = lib.math.divisors(pn)
#     if pn == lib.math.sum_divisors(divs[0:-1]):
#       yield pn
