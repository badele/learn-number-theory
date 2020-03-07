
MAXN=32

import os
import sys

# Add module path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Load math modules
import lib.math
import lib.oeis

a000396_list = enumerate(lib.oeis.a000396_perfect_numbers(MAXN),1)
for n,p in a000396_list:
  print(f'{n} {p}')
