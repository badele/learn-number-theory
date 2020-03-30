import os
import sys
import argparse
import numpy as np

# Add module path
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")))

# Load math modules
import lib.math

MAXN = 100

# Argument options
ap = argparse.ArgumentParser()
ap.add_argument("-g", "--get", choices=['left', 'right'],
                help="get left of right square corner %(default)s)", default="left")
ap.add_argument("-o", "--out", type=str,
                help="save to filename: %(default)s)", default="/tmp/numbers.npy")
ap.add_argument("-p", "--prime",
                help="Only prime: : %(default)s)", action="store_true", default=False)
ap.add_argument("-l", "--level", type=int,
                help="Square level (default: %(default)s)", default=MAXN)
args = vars(ap.parse_args())

from itertools import permutations


maxlevel = args['level']

numbers = []
for n in range(1, maxlevel + 1):
    width = n * 2 - 1
    height = 6 * n - 3

    topleft = 4 * n ** 2
    topright = topleft - width
    bottomleft = topleft - height
    bottomright = bottomleft + width

    if args['get'] == 'left':
        selected = bottomleft
    else:
        selected = topright

    if args['prime']:
        numbers.append(selected)

n = np.array(numbers)
np.save(args['out'], n)
