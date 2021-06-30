import os

CUR_DIR = os.path.abspath(os.path.dirname(__file__))
print(CUR_DIR)
PKG_DIR = os.path.abspath(os.path.join(CUR_DIR, os.pardir))
print(PKG_DIR)

import sys
print(sys.path)
if PKG_DIR not in sys.path:
    sys.path.append(PKG_DIR)