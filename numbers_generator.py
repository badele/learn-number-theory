#!/bin/python

import sys
import json
import sqlite3
import sympy as sp
import matplotlib.pylab as plt

import lib.math

#import matplotlib.pyplot as plt

RANGE=10000
BLOCK=10000
REMAINING=RANGE
# def is_prime_number(n):
#     if n <= 1:
#         return False

#     for i in range(2,n):
#         if (n % i) == 0:
#             return False
#     else:
#         return True

# num
# fp2       computed from square
# fp3       computed from cube
# divisors  all divisors
# nb_div    nb divisors
# nb_divo   odd nb divisors
# sdigit    sum digit number ex: 123 = 6
# sdiv      sum of divisors
# pnumber   perfect number = n == (sdiv - n)

def is_sums_of_three_cubes_compatible(n):
    return n % 9 != 4 and n % 9 != 5

def cube(x,y,z):
    return x**3+y**3+z**3

def solve_sums_of_three_cubes(n,m):
    ax = []
    ay = []
    az = []
    rv = []
    for x in range(m):
        for y in range(m):
            for z in range(m):
                r=cube(x,y,z)
                print(f'{x},{y},{z}')
                print(r)
                ax.append(x)
                ay.append(y)
                az.append(z)
                rv.append(r)
            break
        break

    plt.plot(az,rv)
    plt.show()

# Init Database
conn = sqlite3.connect('nums.db')
c = conn.cursor()
c.execute('DROP TABLE IF EXISTS numbers;')
c.execute('CREATE TABLE numbers(num BIGINT PRIMARY KEY, fp2 BIGINT, fp3 BIGINT, divisors TEXT, nb_div BIGINT, nb_divo BIGINT,sdigit BIGINT, sdiv BIGINT, pnumber BOOLEAN, prime BOOLEAN, pdist BIGINT);')

numlist = []
lastprime = 2
for n in range(0,RANGE):
    num = {'num':n}

    # Sum digit
    num['sdigit'] = lib.math.sum_digit_number(n)


    # Init initial value
    num['fp2'] = -1
    num['fp3'] = -1
    num['pdist'] = -1

    # Prime
    divisors = lib.math.divisors(n)
    num['divisors'] = str(divisors)
    num['nb_div'] = len(divisors)
    num['nb_divo'] = len(divisors) % 2
    num['prime'] = len(divisors)==2
    num['sdiv'] = sum(divisors)


    # Square
    if n>0 and not num['prime']:
        square = n**.5
        intsquare = int(square)
        if square==intsquare:
            num['fp2'] = int(intsquare)

    # Cubic
    if n>0 and not num['prime']:
        r = sp.perfect_power(n,[3])
        if r:
            num['fp3'] = int(r[0])

    num['pnumber'] = n == (num['sdiv'] - n)
    if num['prime']:
        num['pdist'] = n - lastprime
        lastprime = n

    # Is sums_of_three_cubes_compatible
    if not is_sums_of_three_cubes_compatible(n):
        num['not_sums_of_three_cubes_compatible'] = True

    data = (n,num['fp2'],num['fp3'],num['divisors'],num['nb_div'],num['nb_divo'],num['sdigit'],num['sdiv'],num['pnumber'],num['prime'],num['pdist'])
    numlist.append(data)
    if (n % BLOCK) == 0:
        REMAINING -= BLOCK
        print(REMAINING)

c.executemany('INSERT INTO numbers VALUES (?,?,?,?,?,?,?,?,?,?,?)', numlist)
conn.commit()


# for n in range(3):
#     print(f"N:{n}")
#     solve_sums_of_three_cubes(n,10)

# for v in numlist:
#     if 'fp3' in v:
#         print(v)

conn.close()
sys.exit()
