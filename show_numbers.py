import os
import sys
import argparse
import numpy as np
from bitarray import bitarray
import pandas as pd

# Add module path
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")))

# Load math modules
import os
import lib.math

MAXN = 100

# Argument options
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--in", type=str,
                help="load file: %(default)s)", default="/tmp/numbers.npy")
ap.add_argument("-j", "--json",
                help="Export to JSON", action="store_true")
ap.add_argument("-l", "--line", type=int,
                help="select line")
args = vars(ap.parse_args())

# Set numpy print options
rows, columns = os.popen('stty size', 'r').read().split()
np.set_printoptions(threshold=sys.maxsize, linewidth=int(columns))

# Load numbers
numbers = np.load(args['in'])

if args['json']:
    print('{ "primes":' + str(numbers.tolist()) + '}')
    sys.exit(0)

if args['line'] is not None:
    print(numbers[args['line']])
else:
    print(numbers)
