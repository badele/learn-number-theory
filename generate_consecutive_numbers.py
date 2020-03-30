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
ap.add_argument("-i", "--in", type=str,
                help="load file: %(default)s)", default="/tmp/numbers.npy")
ap.add_argument("-o", "--out", type=str,
                help="save file: %(default)s)", default="/tmp/consecutive.npy")
ap.add_argument("-s", "--select", type=int,
                help="select only value", required=True)
args = vars(ap.parse_args())

from sympy import isprime


def zero_runs(a):  # from link
    iszero = np.concatenate(([0], np.equal(a, 0).view(np.int8), [0]))
    absdiff = np.abs(np.diff(iszero))
    ranges = np.where(absdiff == 1)[0].reshape(-1, 2)
    return ranges


# Load numbers
numbers = np.load(args['in'])
result = zero_runs(np.diff(numbers))


# for r in result:
#     print(r)
idx = 0
for r in result:
    try:
        start_pos = r[0]
        end_pos = r[1]
        diff = end_pos - start_pos + 1
        if numbers[start_pos] == args['select']:
            print(f'{diff} :  IDX: {idx}')
        idx += 1
    except:
        pass
# diff = np.diff(result)
# maxi = np.max(diff)
# print(maxi)

np.save(args['out'], result)
