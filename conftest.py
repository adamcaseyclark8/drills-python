import importlib
import os
import sys

# This repo's `code/` package collides with the stdlib `code` module, which
# pdb (and so pytest's debugging plugin) imports. Load pdb against the stdlib
# copy first, then evict it so `from code.<category>.<problem> import ...`
# resolves to the repo.
ROOT = os.path.dirname(os.path.abspath(__file__))
REPO_PATHS = {ROOT, '', '.'}

saved_path = sys.path[:]
sys.path[:] = [p for p in sys.path if os.path.abspath(p or '.') != ROOT and p not in REPO_PATHS]
sys.modules.pop('code', None)
try:
    importlib.import_module('pdb')
finally:
    sys.path[:] = saved_path

sys.modules.pop('code', None)
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
