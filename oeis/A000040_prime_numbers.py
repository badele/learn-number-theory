import os
import sys
import argparse
import numpy as np
from bitarray import bitarray
# Add module path
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")))

# Load math modules
import lib.math

MAXN = 100

# Argument options
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--maxn", type=int,
                help="(default: %(default)s)", default=MAXN)
ap.add_argument("-m", "--method",
                choices=['fast', 'learn'], help="(default: %(default)s)", default='fast')
ap.add_argument("-b", "--bench", help="Active Bench", action='store_true')
ap.add_argument("-s", "--show-sequence",
                help="Show sequence number", action='store_true')
args = vars(ap.parse_args())

# Import function method
if args['method'] == 'fast':
    from lib.oeis.fast import a000040_prime_numbers, a000040_prime_numbers_boolean
else:
    from lib.oeis.learn import a000040_prime_numbers, a000040_prime_numbers_boolean

maxn = args['maxn']

# Compute primes
primes = a000040_prime_numbers(maxn)
print(primes)
lastprime = primes[-1]

data = np.zeros(lastprime + 1)
data[primes] = 1


import matplotlib.pyplot as plt
for idx in range(1, lastprime, 1):
    print(idx)
    GRIDX = idx
    GRIDY = lastprime // idx + 1

    GRIDSIZE = int(idx**0.5) + 1
    maxn = GRIDSIZE**2

    data = np.zeros(GRIDX * GRIDY)
    data[primes] = 1
    data = data.reshape(GRIDY, GRIDX)

    fig, ax = plt.subplots()
    # plt.figure()
    ax.imshow(data)
    ax.grid(True)
    ax.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    # plt.axis('off')

    # for p in primes:
    #     plt.text(p % GRIDX, p // GRIDY, p,
    #              color="w", ha="center", va="center", fontsize=2)

    # plt.show()
    plt.savefig(f'/tmp/result_{idx}.png', dpi=300, bbox_inches='tight')
    plt.close('all')

if not args['bench']:
    for n, p in enumerate(a000040_list, 1):
        if args['show_sequence']:
            print(f'{n} {p}')
        else:
            print(p)
