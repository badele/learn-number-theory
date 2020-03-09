import os
import gc
import sys
import json

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
    pfilename=os.path.join(ROOT,f'.cache/{filename}.cache')
    with open(pfilename, 'w') as f:
        json.dump(datas, f)
