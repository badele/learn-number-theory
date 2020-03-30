import argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import math
import os
import sys

# https://scipython.com/blog/the-ulam-spiral/

# Argument options
WIDTH = 10
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--in", type=str,
                help="load file: %(default)s)", action='append', nargs='*')
ap.add_argument("-o", "--out", type=str,
                help="save file: %(default)s)", default="/tmp/ulam.txt")

ap.add_argument("-w", "--width", type=int,
                help="Matrix size: %(default)s)")

ap.add_argument("-s", "--show",
                help="show", action='store_true')

ap.add_argument("-n", "--normalize",
                help="normalize", action='store_true')
args = vars(ap.parse_args())


def make_spiral(arr):
    nrows, ncols = arr.shape
    idx = np.arange(nrows * ncols).reshape(nrows, ncols)[::-1]
    spiral_idx = []
    while idx.size:
        spiral_idx.append(idx[0])
        # Remove the first row (the one we've just appended to spiral).
        idx = idx[1:]
        # Rotate the rest of the array anticlockwise
        idx = idx.T[::-1]
    # Make a flat array of indices spiralling into the array.
    spiral_idx = np.hstack(spiral_idx)
    # Index into a flattened version of our target array with spiral indices.
    spiral = np.empty_like(arr)
    spiral.flat[spiral_idx] = arr.flat[::-1]
    return spiral


def allnumbers_array(maxn):
    arr = np.arange(1, width**2 + 1, dtype=int)

    return arr


def gen_graph_spiral(arr, width):
    fig = plt.figure(figsize=(width, width))
    plt.matshow(arr, fignum=fig.number, cmap=cm.viridis)
    plt.axis('off')
    plt.savefig('/tmp/result.png', dpi=1)
    plt.show()


def export_to_csv(arr):
    np.savetxt('spiral.csv', arr, delimiter=',', fmt='%d')


# Set numpy print options
rows, columns = os.popen('stty size', 'r').read().split()
np.set_printoptions(threshold=sys.maxsize, linewidth=int(columns))

# init spiral
width = args['width']
arr = np.zeros(width**2, dtype=int)

maxcomputed = 0
idxloop = 2
for filename in args['in']:
    # Load numbers
    numbers = np.load(filename[0])
    maxn = numbers[-1]
    computedwidth = math.ceil(maxn ** 0.5)
    print(f'IDX:{idxloop} file:{filename}: suggest width: {computedwidth}')

    numbers = numbers[numbers <= width**2]

    arr[numbers - 1] = numbers
    # Normalize
    if args['normalize']:
        arr[0] = 1
        arr[numbers - 1] = idxloop
        # arr[1] = 2
        # arr[2] = 3
        # arr[4] = 5

    idxloop += 1


# size = len(arr)
# eulerline = []
# for n in range(1, maxn):
#     eulern = n**2 + n + 41
#     if eulern < size and isprime(eulern):
#         eulerline.append(eulern)

# arr[eulerline] = 2


# All numbers spiral
# arr = allnumbers_array(maxn)

# Make spiral
arr = make_spiral(arr.reshape((args['width'], args['width'])))
arr = np.flipud(arr)
arr = np.rot90(arr, k=2)

# export_to_csv(arr)

np.savetxt(args['out'], arr, fmt='%d')

if args['show']:
    print(arr)

# gen_graph_spiral(arr, width)
