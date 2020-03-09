# import os
# import sys

# # Add module path
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# import lib.math

# # Search perfect square
# def a000290_perfect_square(maxn):
#   for n in range(1,maxn+1):
#       square = n**.5
#       isquare = n//square==square
#       if isquare:
#           yield n

# # def a000290_perfect_square1(maxn):
# #   sieve = [True] * maxn
# #   for i in range(0,maxn+1):
# #     if ((n % i == 0) and (n / i == i)):
