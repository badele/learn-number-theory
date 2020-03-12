import os
import gc
import sys
import json
import numpy as np
from base64 import b64encode, b64decode
from bitarray import bitarray

# Add module path
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)


def load_cache(filename):
    pfilename = os.path.join(ROOT, f'.cache/{filename}.cache')
    if not os.path.exists(pfilename):
        return None

    with open(pfilename, 'r') as f:
        gc.disable()
        datas = json.load(f)
        gc.enable()

    return datas


def save_cache(datas, filename):
    # Create folder if not exists
    folder = os.path.join(ROOT, '.cache')
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Open cache file
    pfilename = os.path.join(folder, f'{filename}.cache')
    with open(pfilename, 'w') as f:
        json.dump(datas, f)

# https://stackoverflow.com/a/35892940/2015612


def load_from_bitarray(filename):
    pfilename = os.path.join(ROOT, f'.cache/{filename}.cache')
    if not os.path.exists(pfilename):
        return None

    datas = bitarray()
    with open(pfilename, 'rb') as f:
        gc.disable()
        datas.fromfile(f)
        gc.enable()

    return datas


# https://stackoverflow.com/a/35892940/2015612
def save_from_bitarray(datas, filename):
    # Create folder if not exists
    folder = os.path.join(ROOT, '.cache')
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Open cache file
    pfilename = os.path.join(folder, f'{filename}.cache')
    with open(pfilename, 'wb') as f:
        datas.tofile(f)


def numpy_load(filename):
    pfilename = os.path.join(ROOT, f'.cache/{filename}.cache')
    if not os.path.exists(pfilename):
        return None

    return np.load(pfilename, allow_pickle=True)


def numpy_save(datas, filename):
    # Create folder if not exists
    folder = os.path.join(ROOT, '.cache')
    if not os.path.exists(folder):
        os.makedirs(folder)

    pfilename = os.path.join(folder, f'{filename}.cache')
    np.save(pfilename, datas, allow_pickle=True)
