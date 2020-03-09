import os
import sys

# Add module path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Load math modules
import lib.math
import lib.oeis

MAXN=10000000

list(lib.oeis.a000290_perfect_square(MAXN))
