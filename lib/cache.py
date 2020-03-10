import os
import gc
import sys
import json
from base64 import b64encode, b64decode
from bitarray import bitarray

# Add module path
ROOT=os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)

def load_cache(filename):
    pfilename=os.path.join(ROOT,f'.cache/{filename}.cache')
    if not os.path.exists(pfilename):
        return None

    with open(pfilename, 'r') as f:
        gc.disable()
        datas = json.load(f)
        gc.enable()

    return datas

def save_cache(datas,filename):
    # Create folder if not exists
    folder = os.path.join(ROOT,'.cache')
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Open cache file
    pfilename=os.path.join(folder,f'{filename}.cache')
    with open(pfilename, 'w') as f:
        json.dump(datas, f)

# https://stackoverflow.com/a/35892940/2015612
def load_from_bitarray(filename):
    pfilename=os.path.join(ROOT,f'.cache/{filename}.cache')
    if not os.path.exists(pfilename):
        return None

    with open(pfilename, 'r') as f:
        gc.disable()
        datas = json.load(f)
        gc.enable()

    ba = bitarray(endian=datas["endian"])
    ba.frombytes(b64decode(datas["bytes"]))
    return ba[:datas["len"]]

# https://stackoverflow.com/a/35892940/2015612
def save_from_bitarray(datas,filename):
    # Create folder if not exists
    folder = os.path.join(ROOT,'.cache')
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Open cache file
    pfilename=os.path.join(folder,f'{filename}.cache')
    with open(pfilename, 'w') as f:
        json.dump({
            "endian": datas.endian(),
            "bytes": str(b64encode(datas.tobytes())),
            "len": len(datas)
        },
        f)
