import os
import sys

from bitarray import bitarray

# Add module path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import lib.math

def fastrange(start,stop,step):
   idx = start
   while idx < stop:
       yield i
       i += step

# Search prime numbers
# https://stackoverflow.com/a/3035188/2015612
def a000040_prime_boolean_numbers(maxn):
  # Try load primes range from cache
  primes = lib.cache.load_from_bitarray(f'primes_{maxn}_boolean')
  if primes is not None:
    return primes

  # Generate primes
  sieve = bitarray(maxn)
  sieve.setall('1')
  for i in range(3,int(maxn**0.5)+1,2):
      if sieve[i]:
          sieve[i**2::2*i] = False

  # Save primes to cache
  lib.cache.save_from_bitarray(sieve,f'primes_{maxn}_boolean')

  return primes


# Search prime numbers
# https://stackoverflow.com/a/3035188/2015612
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
  for p in primes:
    print(f'P: {p}')
    m = 2**p-1
    print(f'm: {m}')
    if isprimes[m]:
      mersenne.append(m)
      print('oui')
    print()

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
